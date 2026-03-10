// lint-and-analyze.js
// Run ESLint and static analysis on all JS/JSX files in the frontend

const { execSync } = require('child_process');
const path = require('path');

function run(command, options = {}) {
  try {
    execSync(command, { stdio: 'inherit', ...options });
  } catch (err) {
    process.exit(1);
  }
}

function main() {
  console.log('--- Running ESLint on frontend JS/JSX files ---');
  run('npx eslint "src/**/*.{js,jsx}" "*.{js,jsx}"');

  console.log('\n--- Running static analysis with import/no-unresolved ---');
  // ESLint with import plugin for static analysis
  run('npx eslint --rule "import/no-unresolved:error" "src/**/*.{js,jsx}" "*.{js,jsx}"');

  console.log('\n--- Lint and static analysis completed ---');
}

main();
