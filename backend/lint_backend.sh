#!/bin/bash

# Install linting tools
pip install ruff black isort

# Run linting checks
ruff check backend/
black --check backend/
isort --check-only backend/
