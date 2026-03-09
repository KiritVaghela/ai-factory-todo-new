const { execSync } = require('child_process');

// Install Vite and necessary plugins
function installDependencies() {
    try {
        console.log('Installing Vite and React plugin...');
        execSync('npm install --save-dev vite @vitejs/plugin-react', { stdio: 'inherit' });
        console.log('Dependencies installed successfully.');
    } catch (error) {
        console.error('Error installing dependencies:', error);
    }
}

installDependencies();
