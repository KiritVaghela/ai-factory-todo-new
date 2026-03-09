// install-dependencies.js

const { exec } = require('child_process');

// Function to install npm dependencies
function installDependencies() {
  exec('npm install', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error installing dependencies: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Error: ${stderr}`);
      return;
    }
    console.log(`Output: ${stdout}`);
  });
}

// Run the function to install dependencies
installDependencies();
