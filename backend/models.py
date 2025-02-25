import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def train_arima_model(df, order=(1, 1, 1)):
    """
    Train an ARIMA model on the provided DataFrame.
    
    Parameters:
        df: pandas DataFrame with a datetime index and a 'Price' column.
        order: tuple, ARIMA order (p, d, q)
    
    Returns:
        model_fit: fitted ARIMA model object.
    """
    # Ensure that the index is datetime; if not, set it from the 'Date' column.
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df['Date'])
    model = ARIMA(df['Price'], order=order)
    model_fit = model.fit()
    return model_fit

def forecast_arima(model_fit, steps=10):
    """
    Forecast future values using the trained ARIMA model.
    
    Parameters:
        model_fit: Fitted ARIMA model object.
        steps: int, number of steps to forecast.
        
    Returns:
        forecast: Forecasted values as a pandas Series.
    """
    forecast = model_fit.forecast(steps=steps)
    return forecast

def train_and_forecast(df, order=(1, 1, 1), forecast_steps=10):
    """
    Convenience function to train an ARIMA model and forecast future values.
    
    Parameters:
        df: DataFrame with oil price data.
        order: tuple, ARIMA order (p,d,q).
        forecast_steps: int, number of steps to forecast.
    
    Returns:
        forecast: Forecasted values as a dictionary.
    """
    df.index = pd.to_datetime(df['Date'])
    df = df.sort_index()
    model_fit = train_arima_model(df, order=order)
    forecast = forecast_arima(model_fit, steps=forecast_steps)
    return forecast.to_dict()
