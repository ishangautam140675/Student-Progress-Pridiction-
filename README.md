Student Performance Prediction using Non-Linear Regression
1. Introduction

Student performance prediction is an important application of machine learning in the education domain.
This project aims to predict student marks based on various factors such as study hours, sleep duration, and attendance.
Since the relationship between these factors and performance is complex, a non-linear regression model is used.

2. Objective

The main objectives of this project are:

To build a machine learning model for predicting student marks
To understand non-linear relationships in data
To develop a simple web application using Flask
To provide user-friendly prediction output

3. Problem Statement

Student performance depends on multiple factors and cannot be accurately predicted using simple linear models.
This project focuses on using a non-linear regression approach to improve prediction accuracy.

4. Methodology
4.1 Data Collection

Sample data is created manually with features such as:

Study Hours
Sleep Hours
Attendance
4.2 Data Preprocessing
Data is structured using Pandas
Features and target variables are separated
4.3 Model Training
Algorithm used: Random Forest Regressor
The model is trained on input data
It learns patterns between features and marks
4.4 Model Saving
The trained model is saved using pickle
File name: model.pkl
4.5 Web Application
Flask is used to create a web interface
User inputs values through a form
Model predicts and displays result

5. System Requirements
Hardware Requirements
Minimum 4GB RAM
Basic computer system
Software Requirements
Python 3.x
Flask
Scikit-learn
Pandas, NumPy

6. Project Structure
student_project/
│
├── app.py
├── train.py
├── model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

7. Implementation
Step 1: Train the Model

Run:

python train.py
Step 2: Run the Application
python app.py
Step 3: Open in Browser
http://127.0.0.1:5000/

8. Results

The model successfully predicts student marks based on input values.
It performs better than linear regression due to its ability to capture non-linear patterns.

9. Advantages
Handles complex relationships
Easy to use web interface
Fast prediction
Reusable model

10. Limitations
Uses small dataset
Accuracy depends on data quality
Limited input features

11. Future Scope
Add more features like previous scores
Improve dataset size
Deploy on cloud platform
Use advanced models like neural networks

12. Conclusion

This project demonstrates the use of non-linear regression in predicting student performance.
It also shows how machine learning models can be integrated into web applications for practical use.

13. References
Scikit-learn Documentation
Flask Documentation
Python Official Documentation
