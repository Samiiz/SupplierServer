import axios from 'axios';

const API_URL = 'http://3.25.100.75:8000/api/v1';

export const signUp = (email, password) => {
  return axios.post(`${API_URL}/signup/`, { email, password });
};

export const login = (email, password) => {
  return axios.post(`${API_URL}/login/`, { email, password });
};

export const getOrders = () => {
  return axios.get(`${API_URL}/orders/`, {
    headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
  });
};
