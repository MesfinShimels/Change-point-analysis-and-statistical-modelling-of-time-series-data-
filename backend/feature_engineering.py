def add_features(df):
    """
    Add feature engineering to the dataset:
    
    - Day of the week.
    - Lag features (previous day's price).
    - 7-day rolling mean.
    - 7-day rolling standard deviation (volatility).
    - Price difference from the previous day.
    
    Parameters:
        df: pandas DataFrame with at least 'Date' and 'Price' columns.
        
    Returns:
        df: pandas DataFrame with new features.
    """
    # Day of the week (0=Monday, 6=Sunday)
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    
    # Lag feature: previous day's price
    df['Lag_1'] = df['Price'].shift(1)
    
    # Rolling features: 7-day rolling mean and standard deviation
    df['RollingMean_7'] = df['Price'].rolling(window=7).mean()
    df['RollingStd_7'] = df['Price'].rolling(window=7).std()
    
    # Price difference from previous day
    df['Diff'] = df['Price'].diff()
    
    # Handle missing values introduced by shifting and rolling
    df = df.fillna(method='bfill')
    
    return df
