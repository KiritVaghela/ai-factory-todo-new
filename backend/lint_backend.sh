#!/bin/bash

# This script runs lint checks on the backend Python code and outputs a report.
# It uses flake8 for linting.

# Exit immediately if a command exits with a non-zero status
set -e

# Define the report file
REPORT_FILE="lint_report.txt"

# Run flake8 linting on the backend directory
# Output both to console and to the report file
flake8 . > "$REPORT_FILE" 2>&1 || true

# Print the lint report summary
if [ -s "$REPORT_FILE" ]; then
  echo "Linting issues found. See $REPORT_FILE for details."
  cat "$REPORT_FILE"
  exit 1
else
  echo "No linting issues found."
  rm -f "$REPORT_FILE"
  exit 0
fi
