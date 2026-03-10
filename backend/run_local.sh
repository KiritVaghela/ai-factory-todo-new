#!/bin/bash
# Run FastAPI backend locally for development

set -e

# Activate virtual environment if exists
test -d venv && source venv/bin/activate

# Export environment variables from .env if exists
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Ensure requirements are installed
pip install --upgrade pip
pip install -r requirements.txt

# Run the FastAPI app
exec uvicorn main:app --reload --host 0.0.0.0 --port 8000
