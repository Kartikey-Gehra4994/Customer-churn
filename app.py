from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

model = joblib.load("models/churn_model.pkl")

columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges']

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = request.form['features']
    feature_l1 = features.split(",")
    data = pd.DataFrame([feature_l1], columns=columns)

    # x = np.array([feature_l1])
    prediction = model.predict(data)[0]

    if prediction == 1:
        result = "Costumer Will Churn"
    else:
        result = "Costumer Will Stay"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)