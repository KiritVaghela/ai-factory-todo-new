#!/bin/bash

# Backend lint script to run lint checks

# Exit immediately if a command exits with a non-zero status
set -e

# Check if pylint is installed
if ! command -v pylint &> /dev/null
then
    echo "pylint could not be found. Please install it with: pip install pylint"
    exit 1
fi

# Run pylint on all Python files in the backend directory
# Exclude __pycache__ directories

# Find all .py files excluding __pycache__ directories
PY_FILES=$(find . -path "*/__pycache__" -prune -o -name "*.py" -print)

if [ -z "$PY_FILES" ]; then
  echo "No Python files found to lint."
  exit 0
fi

# Run pylint and save output to lint_report.txt
pylint $PY_FILES | tee lint_report.txt

# Check pylint exit code
if [ ${PIPESTATUS[0]} -ne 0 ]; then
  echo "Lint errors found. See lint_report.txt for details."
  exit 1
else
  echo "No lint errors found."
fi
