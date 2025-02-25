from data_preparation import load_and_clean_data
from feature_engineering import add_features
from models import train_and_forecast

def get_summary_statistics():
    """
    Loads, cleans, and enriches the oil price data then computes summary statistics.
    
    Returns:
        stats: A dictionary with mean, median, standard deviation, minimum, maximum, and record count.
    """
    df = load_and_clean_data()
    df = add_features(df)
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
    Loads, cleans, and enriches the oil price data then runs an ARIMA forecast.
    
    Returns:
        forecast_values: Forecasted values as a dictionary.
    """
    df = load_and_clean_data()
    df = add_features(df)
    forecast_values = train_and_forecast(df, order=(1, 1, 1), forecast_steps=10)
    return forecast_values
