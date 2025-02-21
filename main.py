from scripts.data_processing import load_and_clean_data, save_processed_data
from scripts.event_detection import detect_events
from scripts.bayesian_model import build_bayesian_model

if __name__ == "__main__":
    # Load and clean data
    raw_data = load_and_clean_data('data/raw/brent_oil_prices.csv')
    save_processed_data(raw_data, 'data/processed/brent_oil_prices_cleaned.csv')
    
    # Detect events
    event_dates = ['2020-03-09', '2022-02-24']  # Example events (COVID-19, Ukraine war)
    processed_data = detect_events(raw_data, event_dates)
    
    # Run Bayesian model
    trace = build_bayesian_model(processed_data['Brent_Price_USD'])
    
    # Save results
    pm.save_trace(trace, 'results/trace.h5')