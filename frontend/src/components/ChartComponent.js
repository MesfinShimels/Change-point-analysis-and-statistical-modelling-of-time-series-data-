import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

function ChartComponent({ forecast }) {
  // Convert forecast object into an array suitable for the chart.
  const data = Object.keys(forecast).map(date => ({
    date,
    forecast: forecast[date]
  }));

  return (
    <LineChart width={600} height={300} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="date" />
      <YAxis />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="forecast" stroke="#8884d8" />
    </LineChart>
  );
}

export default ChartComponent;
