import pandas as pd
import numpy as np
from flask import Flask, request, render_template, url_for, redirect, send_file, make_response
from flask import send_from_directory, current_app
from werkzeug.utils import secure_filename

app = Flask(__name__)


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
    return render_template("predicted_results.html")


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






