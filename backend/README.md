# Backend - FastAPI ToDo API

This is the backend service for the AI Factory ToDo App, built with FastAPI and SQLite.

## Features
- RESTful API for ToDo tasks
- SQLite database
- CORS enabled for frontend integration
- Docker-ready

## Setup Instructions

### 1. Install Python dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Variables

- Copy `.env.example` to `.env` and adjust as needed.

### 3. Initialize the Database

```bash
python db_setup.py
```
This will create the `tasks.db` SQLite database with the required schema.

### 4. Run the API Server

```bash
uvicorn main:app --reload
```
- The API will be available at [http://localhost:8000](http://localhost:8000)

### 5. API Endpoints

- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a new task (JSON: `{ "title": str, "completed": bool }`)
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task
- `OPTIONS /tasks` - CORS preflight

### 6. Running Tests

- Some basic tests are included at the bottom of `main.py` using FastAPI's `TestClient`.
- To run them, use a test runner or run the file directly.

### 7. Troubleshooting Build Errors

- **ModuleNotFoundError:** Ensure all dependencies are installed with `pip install -r requirements.txt`.
- **Database errors:** Make sure to run `python db_setup.py` before starting the server.
- **CORS issues:** The backend is configured to allow all origins by default. Adjust in `main.py` if needed.
- **Port conflicts:** Ensure nothing else is running on port 8000.

### 8. Docker Usage

- The backend can be run as a Docker container. See the root `README.md` for Docker Compose instructions.

---

For frontend integration and full-stack setup, see the root `README.md`.
