from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    sleep = float(request.form['sleep'])
    attendance = float(request.form['attendance'])

    prediction = model.predict([[hours, sleep, attendance]])

    return render_template('index.html', prediction_text=f"Predicted Marks: {prediction[0]:.2f}")

if __name__ == "__main__":
    app.run(debug=True)