import React from 'react';
import ReactDOM from 'react-dom';
import App from './src/App';
import './src/styles.css';

// Check if the root element is present
if (!document.getElementById('root')) {
  throw new Error('Root element not found for React rendering.');
}

// Log to help with debugging
console.log('Starting React Application with Vite configuration');

// Check if Vite command is available in terminal
const checkViteCommand = async () => {
    try {
        const exec = require('child_process').exec;
        exec('vite --version', (error, stdout, stderr) => {
            if (error) {
                console.error(`Error executing vite: ${error.message}`);
                return;
            }
            if (stderr) {
                console.error(`Error: ${stderr}`);
                return;
            }
            console.log(`Vite version: ${stdout}`);
        });
    } catch (err) {
        console.error(`Failed to check vite command: ${err.message}`);
    }
};

checkViteCommand();

// Use Vite's development features
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Adding support for hot module replacement
if (import.meta.hot) {
  import.meta.hot.accept();
}
