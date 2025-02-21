import pandas as pd
from datetime import datetime

def load_and_clean_data(filepath):
    """Load and clean Brent oil price data."""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%B-%y')
    df.rename(columns={'Price': 'Brent_Price_USD'}, inplace=True)
    df.sort_values('Date', inplace=True)
    return df

def save_processed_data(df, output_path):
    """Save cleaned data to CSV."""
    df.to_csv(output_path, index=False)