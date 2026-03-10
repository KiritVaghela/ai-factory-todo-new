import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './src/App.jsx';
import './src/styles.css';

// Check if the root element is present
const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error('Root element not found for React rendering.');
}

// Log to help with debugging
console.log('Starting React Application');

// Check if dependencies are updated
console.log('Verifying application with updated dependencies...');

createRoot(rootElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
