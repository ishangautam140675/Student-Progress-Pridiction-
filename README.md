STUDENT PERFORMANCE PREDICTION USING NON-LINEAR REGRESSION
1. Introduction

Student performance prediction is an important application of Machine Learning in the education sector. The main objective of this project is to predict student marks based on various factors such as study hours, sleep, and attendance. This helps teachers and students understand performance trends and improve outcomes.

In this project, we use a non-linear regression model (Random Forest Regressor), a supervised machine learning algorithm, to predict student performance based on historical data.

2. Objective

The main objectives of this project are:

To understand the concept of supervised learning
To implement a non-linear regression model
To analyze how different factors affect student performance
To build a predictive model for estimating student marks
3. Technology Used
Programming Language: Python
Libraries Used:
Pandas (for data handling)
NumPy (for numerical operations)
Matplotlib (for visualization)
Scikit-learn (for machine learning model)
Flask (for web application)
4. Dataset Description

The dataset contains the following features:

Study Hours
Sleep Hours
Attendance
Marks (Target Variable)

Sample Data:

Study Hours	Sleep Hours	Attendance	Marks
5	7	80	75
8	6	90	88
5. Methodology
Step 1: Data Collection

The dataset is collected in CSV format.

Step 2: Data Preprocessing
Handling missing values (if any)
Selecting features and target variable
Step 3: Splitting Dataset

The dataset is divided into:

Training Data (80%)
Testing Data (20%)
Step 4: Model Training

Random Forest Regressor model is trained using training data.

Step 5: Prediction

The model predicts student marks using test data.

Step 6: Evaluation

Model performance is evaluated using Mean Squared Error.

6. Algorithm Used: Random Forest Regression

Random Forest Regression is used to handle non-linear relationships between variables by combining multiple decision trees.

Mathematical Concept:
Prediction = Average of predictions from multiple decision trees

Where:

Each tree learns patterns from data
Final output is the average of all trees
7. Implementation (Code)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("student_data.csv")

# Features and target
X = data[['StudyHours', 'SleepHours', 'Attendance']]
y = data['Marks']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model training
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
error = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", error)

# Visualization
plt.scatter(y_test, predictions)
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted Marks")
plt.show()

# Custom prediction
sample = [[6, 7, 85]]
predicted_marks = model.predict(sample)
print("Predicted Marks:", predicted_marks)
8. Results

The model successfully predicts student performance based on input features. The prediction accuracy improves due to the use of a non-linear model. The graph between actual and predicted values shows a close relationship.

9. Advantages
Handles non-linear relationships effectively
Provides better accuracy than linear models
Reduces overfitting
Works well with real-world data
10. Limitations
Requires more computation time
Less interpretable compared to linear regression
Performance depends on dataset quality
11. Conclusion

This project demonstrates how a non-linear regression model can be used to predict student performance effectively. It helps in understanding the impact of different study-related factors and provides practical insights.

12. Future Scope
Add more features like previous exam scores
Use advanced models like XGBoost
Improve UI design
Deploy as a web application
