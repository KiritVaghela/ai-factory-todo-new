// This script runs ESLint and Vite build, reporting errors and exiting with nonzero code if any fail.
const { execSync } = require('child_process');

function run(command, label) {
  try {
    console.log(`\n=== Running: ${label} ===`);
    execSync(command, { stdio: 'inherit' });
    console.log(`=== ${label} succeeded ===\n`);
  } catch (err) {
    console.error(`\n=== ${label} failed ===`);
    process.exit(1);
  }
}

// Run ESLint
run('npx eslint src --ext .js,.jsx', 'ESLint');

// Run Vite build
run('npx vite build', 'Vite Build');
