import joblib
import numpy as np
from preprocess import preprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

model = joblib.load('model.joblib')  # Loading the saved model
vectorizer = joblib.load('vectorizer.joblib')  # Loading the saved TF-IDF Vectorizer

@app.route("/predict", methods=["POST"])  # Whenever user POSTs data to "/predict", call this function.
def predict():

    data = request.get_json()  # Reading the incoming JSON data. 

    reviews = data['reviews']  # Extract the review from the dictionary

    process_review = preprocess(reviews)  # Preprocess the review posted

    process_review = vectorizer.transform([process_review])  # Extract features from the review

    prediction = model.predict(process_review) # Predict the sentiment

    return jsonify({"prediction": "positive" if prediction[0] == "1" else "negative"})  # Output the sentiment. jsonify is used to convert python dict to JSON object
    

@app.route("/health", methods=['GET'])  # Used to check if the server is running. It'll output {"status": "ok"} if server is running.
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # app.run(debug=True, host="0.0.0.0", port=5000) # Host: 0.0.0.0 means any computer can connect to this host   
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    