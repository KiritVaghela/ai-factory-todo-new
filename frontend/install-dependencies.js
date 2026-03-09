const { exec } = require('child_process');

// Function to install dependencies
const installDependencies = () => {
  exec('npm install', (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing npm install: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Error: ${stderr}`);
      return;
    }
    console.log(`NPM install output: ${stdout}`);
  });
};

// Run the install function
installDependencies();
