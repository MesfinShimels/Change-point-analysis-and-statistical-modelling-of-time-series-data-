import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def arima_model(df, order=(1, 1, 1), forecast_steps=10):
    """
    Fits an ARIMA model to the oil price data and forecasts future prices.
    
    Parameters:
      - df: DataFrame containing the oil price data.
      - order: ARIMA model order (p, d, q). Default is (1,1,1).
      - forecast_steps: Number of days to forecast. Default is 10.
    
    Returns:
      - A dictionary with forecasted values.
    """
    # Convert the 'Date' column to datetime and set as index.
    df.index = pd.to_datetime(df['Date'], format='%d-%b-%y')
    df = df.sort_index()

    # Fit the ARIMA model.
    model = ARIMA(df['Price'], order=order)
    model_fit = model.fit()

    # Forecast future values.
    forecast = model_fit.forecast(steps=forecast_steps)
    forecast_dict = forecast.to_dict()
    return forecast_dict
