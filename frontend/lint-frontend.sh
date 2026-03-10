#!/bin/bash

# Run ESLint on all JS/JSX/TS/TSX files in src and root
if ! command -v npx &> /dev/null; then
  echo "npx could not be found. Please install Node.js and npm."
  exit 1
fi

# Install dependencies if node_modules is missing
if [ ! -d "node_modules" ]; then
  echo "node_modules not found. Installing dependencies..."
  npm install
fi

# Run ESLint
if [ -f "node_modules/.bin/eslint" ]; then
  echo "Running ESLint..."
  npx eslint src/**/*.jsx src/**/*.js src/**/*.ts src/**/*.tsx index.jsx || exit 1
else
  echo "ESLint is not installed. Installing ESLint..."
  npm install --save-dev eslint
  npx eslint src/**/*.jsx src/**/*.js src/**/*.ts src/**/*.tsx index.jsx || exit 1
fi

echo "Linting completed successfully."
