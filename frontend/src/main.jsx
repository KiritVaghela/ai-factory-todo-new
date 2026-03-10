import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import './styles.css';

// Log to ensure App is being rendered
console.log('Rendering main application...');

// Render the application
const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error('Root element not found for React rendering.');
}

createRoot(rootElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
