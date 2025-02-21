import pandas as pd
import numpy as np

def detect_events(df, event_dates):
    """Correlate price changes with predefined event dates."""
    df['Event'] = np.where(df['Date'].isin(event_dates), 'Yes', 'No')
    return df