import React from 'react';
import SampleComponent from './components/SampleComponent';

function App() {
  console.log('Rendering App component');
  return (
    <div>
      <h1>Simple ToDo App</h1>
      <p>Manage your tasks efficiently!</p>
      <SampleComponent />
    </div>
  );
}

export default App;
