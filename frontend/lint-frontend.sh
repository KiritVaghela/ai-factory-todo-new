#!/bin/bash

# This script runs lint checks for the frontend codebase

# Exit immediately if a command exits with a non-zero status
set -e

# Check if node_modules exists, if not, prompt to install dependencies
if [ ! -d "node_modules" ]; then
  echo "node_modules directory not found. Please run 'npm install' first."
  exit 1
fi

# Run ESLint on the src directory
npx eslint "src/**/*.{js,jsx,ts,tsx}" --max-warnings=0

# You can add more linting commands here if needed

# Success message
echo "Frontend linting passed successfully!"
