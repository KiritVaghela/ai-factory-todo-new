# Backend

This directory contains the backend code for the ToDo application.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Initialize the database:

```bash
python db_setup.py
```

4. Run the backend server:

```bash
uvicorn main:app --reload
```

## Linting

To check the backend code for linting issues, run the following command:

```bash
./lint_backend.sh
```

This script runs linting tools to ensure code quality and consistency.

## Environment Variables

- Copy `.env.example` to `.env` and update the variables as needed.

## API Endpoints

- `/tasks/` - GET, POST, PUT, DELETE operations for tasks.

## Notes

- The backend uses FastAPI and SQLite.
- CORS is enabled for all origins.
