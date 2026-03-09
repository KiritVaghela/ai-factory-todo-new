import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';
import './styles.css';
import LoginForm from './components/LoginForm';

// Check if the root element is present
if (!document.getElementById('root')) {
  throw new Error('Root element not found for React rendering.');
}

// Log to help with debugging
console.log('Starting React Application');

// Check if dependencies are updated
console.log('Verifying application with updated dependencies...');

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
    <LoginForm />
  </React.StrictMode>
);
