from flask import Flask, jsonify
from analysis import get_summary_statistics, run_arima_forecast

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

if __name__ == '__main__':
    app.run(debug=True)
