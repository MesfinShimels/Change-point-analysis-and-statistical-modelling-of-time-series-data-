import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_trend(df):
    """
    Plot the time series trend of Brent oil prices.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing 'Date' and 'Price'.
    """
    plt.figure(figsize=(12,6))
    sns.lineplot(data=df, x='Date', y='Price')
    plt.title("Brent Oil Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    plt.show()

def compute_moving_average(df, window=30):
    """
    Compute the moving average of the oil price.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing 'Price'.
        window (int): The window size for the moving average.
        
    Returns:
        pd.DataFrame: DataFrame with a new 'Moving_Avg' column.
    """
    df['Moving_Avg'] = df['Price'].rolling(window=window).mean()
    return df
