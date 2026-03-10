#!/bin/bash

set -e

cd "$(dirname "$0")"

# Lint with flake8
if ! command -v flake8 >/dev/null 2>&1; then
    echo "flake8 not found. Installing..."
    pip install flake8
fi

# Type check with mypy
if ! command -v mypy >/dev/null 2>&1; then
    echo "mypy not found. Installing..."
    pip install mypy
fi

# Run flake8
echo "Running flake8 linter..."
flake8 . --exclude=tasks.db,__pycache__,.env,.env.example

# Run mypy
echo "Running mypy static type checker..."
mypy . --ignore-missing-imports --exclude tasks.db
