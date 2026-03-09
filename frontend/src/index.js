import React from 'react';
import ReactDOM from 'react-dom';
import App from './src/App';
import './src/styles.css';
import LoginForm from './components/LoginForm';

// Check if the root element is present
if (!document.getElementById('root')) {
  throw new Error('Root element not found for React rendering.');
}

// Log to help with debugging
console.log('Starting React Application');

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
    <LoginForm />
  </React.StrictMode>
);
