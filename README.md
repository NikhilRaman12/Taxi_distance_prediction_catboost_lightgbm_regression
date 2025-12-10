
# Taxi Trip Distance Prediction (CatBoost + LightGBM Regression)

## Overview
This project builds a regression model to predict taxi trip distances using an ensemble of CatBoost and LightGBM. The goal is to deliver accurate predictions while avoiding data leakage and ensuring reproducibility.

## Dataset
- **Train.csv**: Training dataset with features and target values.
- **Test.csv**: Test dataset for evaluation.
- **submission.csv**: Sample submission file with predicted distances.

## Approach
1. **Feature Engineering**
   - Extracted time-based features (hour, day, weekday).
   - Derived geospatial features (haversine distance, bearing).
   - Applied leakage avoidance strategies.

2. **Modeling**
   - CatBoost and LightGBM regressors trained separately.
   - Predictions combined via weighted stacking.
   - Hyperparameters tuned for leaderboard performance.

3. **Evaluation**
   - Metrics: RMSE and MAE.
   - Cross-validation to ensure robustness.

## Repository Structure

## Usage
Clone the repository and run the notebook or scripts in your environment:
```bash
git clone https://github.com/NikhilRaman12/Taxi_distance_prediction_catboost_lightgbm_regression.git
cd Taxi_distance_prediction_catboost_lightgbm_regression
```
