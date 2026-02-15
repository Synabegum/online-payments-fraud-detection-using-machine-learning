# app.py

from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("model/model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    prediction = model.predict(final_features)

    if prediction[0] == 1:
        result = "Fraudulent Transaction 🚨"
    else:
        result = "Legitimate Transaction ✅"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
