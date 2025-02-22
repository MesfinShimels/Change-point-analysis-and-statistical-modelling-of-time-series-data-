import pandas as pd
import matplotlib.pyplot as plt

def plot_forecast(df, forecast, title="Forecast"):
    """
    Plot the historical Brent oil prices along with the forecast.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing historical data.
        forecast (array-like): Forecasted prices.
        title (str): Title for the plot.
    """
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Price'], label="Historical Prices")
    # Generate future dates based on the last available date
    future_dates = pd.date_range(start=df['Date'].iloc[-1], periods=len(forecast)+1, freq='D')[1:]
    plt.plot(future_dates, forecast, label="Forecast", linestyle='--')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()
