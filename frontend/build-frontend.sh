#!/bin/bash

# Build the frontend using Vite
if ! command -v npx &> /dev/null; then
  echo "npx could not be found. Please install Node.js and npm."
  exit 1
fi

# Install dependencies if node_modules is missing
if [ ! -d "node_modules" ]; then
  echo "node_modules not found. Installing dependencies..."
  npm install
fi

# Run Vite build
if [ -f "node_modules/.bin/vite" ]; then
  echo "Running Vite build..."
  npx vite build || exit 1
else
  echo "Vite is not installed. Installing Vite..."
  npm install --save-dev vite
  npx vite build || exit 1
fi

echo "Frontend build completed successfully."
