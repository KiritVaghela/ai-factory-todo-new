import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

const getToken = () => {
  return localStorage.getItem('jwt_token');
};

const fetchWithAuth = (url, options = {}) => {
  const token = getToken();
  if (token) {
    options.headers = {
      ...options.headers,
      'Authorization': `Bearer ${token}`
    };
  }
  return fetch(url, options);
};

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App fetchWithAuth={fetchWithAuth} />
  </React.StrictMode>,
);