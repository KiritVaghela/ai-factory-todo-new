import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css';

// Function to set JWT token in localStorage
const setJwtToken = (token) => {
  localStorage.setItem('jwtToken', token);
};

// Simulated login function (replace with actual login logic)
const login = async () => {
  const token = 'example.jwt.token'; // This should come from your backend login response
  setJwtToken(token);
};

login(); // Call login to demonstrate setting token

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);