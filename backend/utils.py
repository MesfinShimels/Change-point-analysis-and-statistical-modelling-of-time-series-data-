import pandas as pd
import os

def load_data():
    """
    Loads the Brent oil prices CSV file into a Pandas DataFrame.
    Assumes the CSV file is located in the ../data/ directory.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '..', 'data', 'brent_oil_prices.csv')
    df = pd.read_csv(file_path)
    return df
