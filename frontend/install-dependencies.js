// install-dependencies.js
const { exec } = require('child_process');

// Function to run npm install
function installDependencies() {
    exec('npm install', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error during npm install: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return;
        }
        console.log(`stdout: ${stdout}`);
    });
}

// Export the function to use elsewhere in the project
module.exports = installDependencies;
