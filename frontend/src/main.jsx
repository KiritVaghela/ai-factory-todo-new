import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css';
import LoginForm from './components/LoginForm';

const MainComponent = () => {
  return (
    <>
      <LoginForm />
      <App />
    </>
  );
};

ReactDOM.render(
  <React.StrictMode>
    <MainComponent />
  </React.StrictMode>,
  document.getElementById('root')
);