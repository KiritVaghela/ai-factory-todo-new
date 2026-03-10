#!/bin/bash
# Lint and type check backend Python code

set -e

cd "$(dirname "$0")"

# Install dependencies if not present
if ! command -v flake8 &> /dev/null; then
    echo "flake8 not found, installing..."
    pip install flake8
fi
if ! command -v mypy &> /dev/null; then
    echo "mypy not found, installing..."
    pip install mypy
fi

# Run flake8
echo "Running flake8..."
flake8 . > lint_report.txt || true

# Run mypy
echo "Running mypy..."
mypy . >> lint_report.txt || true

echo "Lint and type check complete. See lint_report.txt for details."
