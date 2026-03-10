// This script checks if node_modules exists and if dependencies are up to date.
// If not, it runs 'npm install'.

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function checkNodeModules() {
  const nodeModulesPath = path.join(__dirname, 'node_modules');
  return fs.existsSync(nodeModulesPath);
}

function checkPackageLock() {
  const lockPath = path.join(__dirname, 'package-lock.json');
  return fs.existsSync(lockPath);
}

function checkOutdated() {
  try {
    const result = execSync('npm outdated --json', { encoding: 'utf8' });
    if (result && result.trim() !== '{}') {
      return true;
    }
    return false;
  } catch (err) {
    // If npm outdated exits with code 1, it means there are outdated packages
    if (err.stdout && err.stdout.trim() !== '{}') {
      return true;
    }
    return false;
  }
}

function installDependencies() {
  console.log('Installing/updating frontend dependencies...');
  execSync('npm install', { stdio: 'inherit' });
}

function main() {
  const hasNodeModules = checkNodeModules();
  const hasLock = checkPackageLock();
  const isOutdated = checkOutdated();

  if (!hasNodeModules || !hasLock || isOutdated) {
    installDependencies();
  } else {
    console.log('Frontend dependencies are installed and up to date.');
  }
}

main();
