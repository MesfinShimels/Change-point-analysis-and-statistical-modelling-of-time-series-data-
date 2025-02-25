import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ChartComponent from './ChartComponent';

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [forecast, setForecast] = useState(null);

  useEffect(() => {
    // Fetch summary data from the backend
    axios.get('http://localhost:5000/api/summary')
      .then(response => setSummary(response.data))
      .catch(error => console.error("Error fetching summary:", error));

    // Fetch forecast data from the backend
    axios.get('http://localhost:5000/api/forecast')
      .then(response => setForecast(response.data))
      .catch(error => console.error("Error fetching forecast:", error));
  }, []);

  return (
    <div>
      <h2>Summary Statistics</h2>
      {summary ? (
        <ul>
          <li>Mean Price: {summary.mean.toFixed(2)}</li>
          <li>Median Price: {summary.median.toFixed(2)}</li>
          <li>Standard Deviation: {summary.std.toFixed(2)}</li>
          <li>Minimum Price: {summary.min.toFixed(2)}</li>
          <li>Maximum Price: {summary.max.toFixed(2)}</li>
          <li>Total Records: {summary.count}</li>
        </ul>
      ) : (
        <p>Loading summary statistics...</p>
      )}

      <h2>ARIMA Forecast</h2>
      {forecast ? (
        <ChartComponent forecast={forecast} />
      ) : (
        <p>Loading forecast data...</p>
      )}
    </div>
  );
}

export default Dashboard;
