import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Sample dataset (you can replace with CSV)
data = {
    'hours_study': [1,2,3,4,5,6,7,8],
    'sleep_hours': [6,7,8,5,6,7,8,6],
    'attendance': [60,70,75,80,85,90,95,100],
    'marks': [50,55,65,70,75,85,90,95]
}

df = pd.DataFrame(data)

X = df[['hours_study', 'sleep_hours', 'attendance']]
y = df['marks']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model Trained & Saved ✅")