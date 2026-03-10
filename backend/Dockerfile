FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv or pip
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install flake8 for linting
RUN pip install --no-cache-dir flake8

# Copy backend source code
COPY backend/ ./

# Expose port
EXPOSE 8000

# Default command
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Add lint target as an argument for convenience
# Usage: docker build --target lint .

FROM python:3.11-slim as lint
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir flake8
COPY backend/ ./

# Run flake8 lint
CMD ["flake8", "."]
