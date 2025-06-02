// frontend/src/services/api.js

import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:5000';

export const getProcesses = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/processes`);
    return response.data;
  } catch (error) {
    console.error('API error:', error);
    throw error;
  }
};
