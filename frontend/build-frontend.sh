#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
npm install

# Build the frontend
npm run build

# Verify the build
if [ -d "dist" ]; then
  echo "Frontend build successful!"
else
  echo "Frontend build failed!"
  exit 1
fi
