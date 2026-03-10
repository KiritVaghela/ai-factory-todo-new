#!/bin/bash
set -e

# Run flake8
echo "Running flake8..."
flake8 .

# Run mypy
echo "Running mypy..."
mypy .
