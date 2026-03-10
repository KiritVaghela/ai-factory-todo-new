# Backend - FastAPI ToDo App

This is the backend service for the ToDo application, built with FastAPI and SQLite.

## Requirements

- Python 3.8+
- pip

## Setup Instructions

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

4. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
   - The API will be available at [http://localhost:8000](http://localhost:8000)
   - API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## Running with Docker

If you prefer Docker, run from the project root:

```bash
docker-compose up --build
```

## Notes

- **CORS:** The backend is configured to allow all origins for development. Adjust `allow_origins` in `main.py` for production.
- **Database:** If you delete `tasks.db`, rerun `python db_setup.py` to recreate the database.

## Testing

- The backend includes basic tests in `main.py` using FastAPI's `TestClient`.
- To run tests, use `pytest` or run the file directly.

---

## License

MIT License
