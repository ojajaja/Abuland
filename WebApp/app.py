from flask import Flask, render_template, request, jsonify
from pycaret.regression import *
from sklearn.preprocessing import *
import numpy as np
import pandas as pd
from joblib import load

data = pd.read_csv("Abuland\WebApp\static\Cleaned_Rice_Data.csv")
data = data.drop(columns=['RiceCons'])
data_cols = data.columns

rc_clf = load("Abuland\WebApp\static\RC_Predict.pkl")


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        int_features = [x for x in request.form.values()]
        final = np.array([int_features])  # Wrap int_features in another list to make it a single row
        data_unseen = pd.DataFrame(final, columns=data_cols)
        prediction = predict_model(rc_clf, data_unseen, round=0)
        # print(prediction)
        pred_label = prediction['prediction_label'][0]
        # pred_score = prediction['prediction_score'][0]

        return render_template("index.html", label=pred_label, submitted=True)
    else:
        return render_template("index.html", submitted=False)
    
@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    if request.method == "POST":
        int_features = [x for x in request.form.values()]
        final = np.array([int_features])  # Wrap int_features in another list to make it a single row
        data_unseen = pd.DataFrame(final, columns=data_cols)
        prediction = predict_model(rc_clf, data_unseen, round=0)
        # print(prediction)
        pred_label = prediction['prediction_label'][0]
        # pred_score = prediction['prediction_score'][0]

        return render_template("index.html", label=pred_label, submitted=True)
    else:
        return render_template("index.html", submitted=False)


if __name__ == '__main__':
    app.run(debug=True)
