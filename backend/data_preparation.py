import pandas as pd
import os

def load_and_clean_data(file_path=None):
    """
    Load and clean the Brent oil prices data.
    
    - Converts 'Date' to datetime.
    - Removes duplicates.
    - Handles missing values.
    - Sorts the data by date.
    
    Parameters:
        file_path: (str) Path to the CSV file. If None, defaults to data/brent_oil_prices.csv.
        
    Returns:
        df: Cleaned pandas DataFrame.
    """
    if file_path is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '..', 'data', 'brent_oil_prices.csv')
    
    df = pd.read_csv(file_path)
    
    # Convert 'Date' column to datetime; handle conversion errors gracefully
    try:
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
    except Exception as e:
        print("Error converting 'Date':", e)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Remove duplicate records
    df = df.drop_duplicates()
    
    # Drop rows where 'Date' or 'Price' is missing
    df = df.dropna(subset=['Date', 'Price'])
    
    # Ensure Price is numeric
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df = df.dropna(subset=['Price'])
    
    # Sort the data by Date
    df = df.sort_values(by='Date')
    
    return df
