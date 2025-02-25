from flask import Flask, jsonify
from analysis import get_summary_statistics, run_arima_forecast
from model_training import train_and_evaluate_model

app = Flask(__name__)

@app.route('/api/summary', methods=['GET'])
def summary():
    """Endpoint to return summary statistics of Brent oil prices."""
    summary_stats = get_summary_statistics()
    return jsonify(summary_stats)

@app.route('/api/forecast', methods=['GET'])
def forecast():
    """Endpoint to return ARIMA forecast data."""
    forecast_data = run_arima_forecast()
    return jsonify(forecast_data)

@app.route('/api/train', methods=['GET'])
def train_model():
    """Endpoint to train the ARIMA model and return evaluation metrics."""
    _, _, metrics = train_and_evaluate_model()
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(debug=True)
