import pandas as pd
from models import arima_model
from utils import load_data

def get_summary_statistics():
    """
    Loads the oil price data and computes basic summary statistics.
    Returns a dictionary with mean, median, standard deviation, etc.
    """
    df = load_data()
    stats = {
        "mean": df['Price'].mean(),
        "median": df['Price'].median(),
        "std": df['Price'].std(),
        "min": df['Price'].min(),
        "max": df['Price'].max(),
        "count": int(df['Price'].count())
    }
    return stats

def run_arima_forecast():
    """
    Loads the oil price data and applies an ARIMA model forecast.
    Returns forecasted values as a dictionary.
    """
    df = load_data()
    forecast_values = arima_model(df)
    return forecast_values
