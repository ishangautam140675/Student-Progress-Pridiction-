Student Performance Prediction (Non-Linear Regression)
About the Project

This project predicts student marks based on study-related factors like study hours, sleep, and attendance.
A non-linear regression model (Random Forest) is used because the relationship between these factors and marks is not strictly linear.

Technologies Used
Python
Scikit-learn
Flask
HTML, CSS
Pandas, NumPy
Project Structure
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
How It Works
Data is used to train a machine learning model
The trained model is saved as model.pkl
Flask loads the model
User enters input in the web form
Model predicts marks and shows result
Model Used

Random Forest Regressor

Reason: It handles non-linear relationships better than simple linear regression.

Input Features
Study Hours
Sleep Hours
Attendance
Output
Predicted student marks

