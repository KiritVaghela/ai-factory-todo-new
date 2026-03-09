const { exec } = require('child_process');

// Function to run npm install
function installDependencies() {
    exec('npm install', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing npm install: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`npm install stderr: ${stderr}`);
            return;
        }
        console.log(`npm install stdout: ${stdout}`);
    });
}

// Execute the function to install dependencies
installDependencies();
