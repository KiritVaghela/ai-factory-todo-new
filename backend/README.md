# Backend - FastAPI ToDo App

This is the backend service for the ToDo application, built with FastAPI and SQLite.

## Requirements

- Python 3.8+
- pip

## Setup

1. **Install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   - Copy `.env.example` to `.env` and adjust as needed.

3. **Initialize the database:**
   ```bash
   python db_setup.py
   ```
   This will create `tasks.db` with the required tables.

4. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```
   - The API will be available at [http://localhost:8000](http://localhost:8000)
   - API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints

- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## CORS

CORS is enabled for all origins in development. Adjust `allow_origins` in `main.py` for production.

## Testing

Run tests using pytest:
```bash
pytest main.py
```

## Database

- Uses SQLite (`tasks.db`) by default.
- To reset the database, delete `tasks.db` and rerun `python db_setup.py`.

## Troubleshooting

- Ensure the virtual environment is activated before running commands.
- If you get CORS errors, make sure the frontend is running on the correct port and the backend CORS settings allow it.
