import pandas as pd

def load_data(filepath):
    """
    Load the Brent oil prices CSV file.
    
    Parameters:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: DataFrame with parsed dates.
    """
    df = pd.read_csv(filepath, parse_dates=['Date'], dayfirst=True)
    return df

def clean_data(df):
    """
    Clean the dataset by removing missing values and sorting by date.
    
    Parameters:
        df (pd.DataFrame): Raw data DataFrame.
        
    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = df.dropna()
    df = df.sort_values('Date')
    return df

if __name__ == '__main__':
    data_path = 'data/raw/brent_oil_prices.csv'
    df = load_data(data_path)
    df_clean = clean_data(df)
    # Save the cleaned data for further analysis
    df_clean.to_csv('data/processed/brent_oil_prices_clean.csv', index=False)
