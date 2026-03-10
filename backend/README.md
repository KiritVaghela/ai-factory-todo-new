# Backend - FastAPI

This is the backend service for the ToDo App, built with FastAPI and SQLite.

## Requirements

- Python 3.11+
- (Recommended) Virtual environment

## Setup

1. **Install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   - Copy `.env.example` to `.env` and adjust as needed.

3. **Set up the database:**
   ```bash
   python db_setup.py
   ```
   - This will create `tasks.db` with the required tables.

4. **Run the server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   - The API will be available at [http://localhost:8000](http://localhost:8000)
   - API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints

- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## CORS

CORS is enabled for all origins by default (see `main.py`). Adjust as needed for production.

## Linting

- Example: `flake8 main.py`
- Lint report: see `lint_report.txt`

## Testing

- (Add tests as needed)

## Running with Docker

- The backend is included in the root `docker-compose.yml` for easy orchestration.

---

## Troubleshooting

- If you change dependencies, rebuild Docker images: `docker-compose build --no-cache`
- If you change the database schema, rerun `db_setup.py` (may require deleting `tasks.db` for a fresh start).
