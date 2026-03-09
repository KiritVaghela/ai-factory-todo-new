import React from 'react';
import ReactDOM from 'react-dom';
import App from './src/App';
import './src/styles.css';

// Check if the root element is present
if (!document.getElementById('root')) {
  throw new Error('Root element not found for React rendering.');
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
