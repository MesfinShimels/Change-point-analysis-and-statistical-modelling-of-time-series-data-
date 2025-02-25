import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const fetchSummary = () => axios.get(`${API_BASE_URL}/summary`);

export const fetchForecast = () => axios.get(`${API_BASE_URL}/forecast`);
