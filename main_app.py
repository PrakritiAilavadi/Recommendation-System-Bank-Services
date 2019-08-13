import csv

import pandas as pd
import numpy as np
from flask import Flask, request, render_template, url_for, redirect, send_file, make_response
from flask import send_from_directory, current_app
from werkzeug.utils import secure_filename
import os
import pickle
import sklearn


UPLOAD_FOLDER = 'C:/Users/rbs/PycharmProjects/recommendation_sys/folder'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route("/")
def index(user=None):
    return render_template("homepage.html", user=user)


@app.route("/get_customer_details", methods=['GET', 'POST'])
def customer_details():
    return render_template("customer_details.html")


@app.route("/train_model", methods=['GET', 'POST'])
def train_model():
    return render_template("train_model.html")


@app.route("/predicted_results", methods=['GET', 'POST'])
def predicted_results():
    x_test = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], 'x_test.csv'))
    if request.method == 'POST':
        customer_id = request.form['CustomerID']

    csv_file = csv.reader(open(os.path.join(app.config['UPLOAD_FOLDER'], 'x_test.csv')), delimiter=",")

    # fetching details of customer from x_test
    for row in csv_file:
        if customer_id == row[1]:
            print(row)
            break

    data = row[1:]
    data = list(map(int, data))
    print(data)
    model = pickle.load(open('logistics_regression_model_mortgage.sav', 'rb'))
    predicted_output = model.predict_proba([data])[:, 1]
    print(predicted_output)
    predicted_output = round(predicted_output[0]*100, 2)
    predicted_mortgage = (predicted_output >= 80.00)
    # print(predicted_output)
    return render_template("predicted_results.html", array_details=row, mortgage=predicted_mortgage,
                           score=predicted_output)


@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        file = request.files['file']
        filename = secure_filename(file.filename)
        # global var
        # var = filename
        # df.to_csv(np.os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # global flag
        # flag = "file_upload"
        return render_template("train_model.html")






if __name__ == "__main__":
    app.run(debug=True)






