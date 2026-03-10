#!/bin/bash

# This script runs both backend and frontend code validation

# Run backend lint
echo "Running backend lint..."
./backend/lint.sh
BACKEND_LINT_EXIT_CODE=$?

# Run frontend lint
echo "Running frontend lint..."
./frontend/lint.sh
FRONTEND_LINT_EXIT_CODE=$?

if [ $BACKEND_LINT_EXIT_CODE -eq 0 ] && [ $FRONTEND_LINT_EXIT_CODE -eq 0 ]; then
  echo "All validations passed successfully."
  exit 0
else
  echo "Validation failed."
  exit 1
fi
