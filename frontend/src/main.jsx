import React from 'react';
import ReactDOM from 'react-dom';
import App from './app';
import './styles.css';

// Render the application
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Ensure that App is imported and rendered correctly