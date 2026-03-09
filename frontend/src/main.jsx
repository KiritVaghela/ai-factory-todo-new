import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';
import './styles.css';

// Log to ensure App is being rendered
console.log('Rendering main application...');

// Render the application
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
