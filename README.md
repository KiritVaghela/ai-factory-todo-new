# AI Factory ToDo App

This is a full-stack ToDo application built with FastAPI (Python) for the backend and React (Vite) for the frontend. It uses SQLite for data storage and Docker for containerization.

## Project Structure

```
ai-factory-todo-new/
  README.md
  docker-compose.yml
  Dockerfile
  backend/
    README.md
    requirements.txt
    db_setup.py
    main.py
    models.py
    .env.example
    .env
    tasks.db
    routers/
      tasks.py
  frontend/
    vite.config.js
    index.css
    index.html
    tailwind.config.js
    package.json
    .babelrc
    package-lock.json
    babel.config.js
    index.jsx
    install-dependencies.js
    test/
      setupTests.js
      build.test.js
      npm_start.test.js
    src/
      main.jsx
      styles.css
      DeleteButton.jsx
      App.jsx
      TaskList.jsx
```

## Quick Start

### Prerequisites
- Docker & Docker Compose (recommended)
- Python 3.8+
- Node.js 16+

### 1. Clone the repository
```
git clone <repo-url>
cd ai-factory-todo-new
```

### 2. Backend Setup

#### a. Using Docker (Recommended)

```
docker-compose up --build
```

This will build and start both the backend and frontend services.

#### b. Manual Setup

1. **Install Python dependencies:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Set up the database:**
   ```bash
   python db_setup.py
   ```
3. **Run the backend server:**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at [http://localhost:8000](http://localhost:8000)

### 3. Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```
2. **Start the development server:**
   ```bash
   npm run dev
   ```
   The app will be available at [http://localhost:3000](http://localhost:3000)

### 4. API Endpoints
- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

### 5. Troubleshooting Build Errors

- **Backend:**
  - Ensure you have Python 3.8+ and `pip` installed.
  - If you see `ModuleNotFoundError`, run `pip install -r requirements.txt` again.
  - If the database is missing, run `python db_setup.py` in the `backend` directory.
  - For CORS issues, the backend is configured to allow all origins by default. Adjust in `main.py` if needed.

- **Frontend:**
  - Ensure Node.js 16+ is installed.
  - If you see dependency errors, run `npm install` again in the `frontend` directory.
  - If the app does not load, check the backend is running at `localhost:8000`.

- **Docker:**
  - If you encounter build errors, try `docker-compose down -v` to remove volumes and rebuild with `docker-compose up --build`.

### 6. Environment Variables
- Copy `.env.example` to `.env` in the `backend` directory and adjust as needed.

### 7. Running Tests
- Backend tests are included in `main.py` using FastAPI's `TestClient`.
- Frontend tests are in `frontend/test/`.

---

For more details, see the `backend/README.md`.
