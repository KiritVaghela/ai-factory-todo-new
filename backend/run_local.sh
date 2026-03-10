#!/bin/bash
# Run the FastAPI backend locally

export PYTHONPATH=$(pwd)

if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
