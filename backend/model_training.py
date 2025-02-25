import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from data_preparation import load_and_clean_data
from feature_engineering import add_features
from models import train_arima_model, forecast_arima

def train_and_evaluate_model(order=(1, 1, 1)):
    """
    Train an ARIMA model on the cleaned oil price data and evaluate its performance.
    
    Steps:
      - Load and clean the data.
      - Add engineered features.
      - Split data into training (80%) and testing (20%) sets.
      - Train the ARIMA model on the training set.
      - Forecast on the testing set.
      - Evaluate the forecast using MAE and RMSE.
    
    Returns:
        model_fit: The fitted ARIMA model.
        forecast: Forecasted values (pandas Series) for the test set.
        metrics: Dictionary with evaluation metrics (MAE and RMSE).
    """
    # Load and prepare data
    df = load_and_clean_data()
    df = add_features(df)
    
    # Split data (80% train, 20% test)
    split_index = int(len(df) * 0.8)
    train = df.iloc[:split_index].copy()
    test = df.iloc[split_index:].copy()
    
    # Ensure datetime index for both train and test sets
    train.index = pd.to_datetime(train['Date'])
    test.index = pd.to_datetime(test['Date'])
    
    # Train ARIMA model on the training set
    model_fit = train_arima_model(train, order=order)
    
    # Forecast for the test set period
    forecast = forecast_arima(model_fit, steps=len(test))
    
    # Calculate evaluation metrics
    mae = mean_absolute_error(test['Price'], forecast)
    rmse = np.sqrt(mean_squared_error(test['Price'], forecast))
    metrics = {"MAE": mae, "RMSE": rmse}
    
    return model_fit, forecast, metrics

if __name__ == "__main__":
    model_fit, forecast, metrics = train_and_evaluate_model()
    print("Evaluation Metrics:", metrics)
    print("Forecast values:", forecast.to_dict())
