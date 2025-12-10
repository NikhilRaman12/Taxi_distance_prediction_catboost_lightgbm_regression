%%writefile main.py
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load data
train = pd.read_csv("Train.csv")
test = pd.read_csv("Test.csv")

# Example feature engineering (replace with your logic)
X = train.drop(columns=["trip_distance"])
y = train["trip_distance"]

# Train/test split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train CatBoost
cb = CatBoostRegressor(verbose=0, random_state=42)
cb.fit(X_train, y_train)

# Train LightGBM
lgb = LGBMRegressor(random_state=42)
lgb.fit(X_train, y_train)

# Ensemble predictions
val_preds = 0.5 * cb.predict(X_val) + 0.5 * lgb.predict(X_val)
print("Validation RMSE:", mean_squared_error(y_val, val_preds, squared=False))

# Predict on test set
test_preds = 0.5 * cb.predict(test) + 0.5 * lgb.predict(test)

# Save submission
submission = pd.DataFrame({"tripid": test["tripid"], "distance": test_preds})
submission.to_csv("submission.csv", index=False)
print("Submission file created: submission.csv")
