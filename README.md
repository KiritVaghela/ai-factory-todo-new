# ToDo App - AI Factory

This is a full-stack ToDo application built with FastAPI (Python) for the backend and React (Vite) for the frontend. It uses SQLite for data storage and Docker for easy deployment.

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

## Prerequisites

- [Docker](https://www.docker.com/) (recommended for easiest setup)
- [Python 3.8+](https://www.python.org/) (if running backend locally)
- [Node.js 16+](https://nodejs.org/) and [npm](https://www.npmjs.com/) (if running frontend locally)

---

## Quick Start with Docker

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd ai-factory-todo-new
   ```

2. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```
   - The backend will be available at [http://localhost:8000](http://localhost:8000)
   - The frontend will be available at [http://localhost:3000](http://localhost:3000)

---

## Running Backend Locally

1. **Install dependencies:**
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

3. **Run the FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```
   - The API will be available at [http://localhost:8000](http://localhost:8000)
   - API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Running Frontend Locally

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```
   Or run the helper script:
   ```bash
   node install-dependencies.js
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```
   - The app will open at [http://localhost:3000](http://localhost:3000)

---

## Environment Variables

- Backend uses a `.env` file for configuration. See `backend/.env.example` for reference.
- By default, the backend uses SQLite (`tasks.db`).

---

## Testing

### Backend
- Run tests (from `backend/`):
  ```bash
  pytest main.py
  ```

### Frontend
- Run tests (from `frontend/`):
  ```bash
  npm test
  ```

---

## Notes

- **CORS:** The backend is configured to allow all origins for development. Adjust `allow_origins` in `backend/main.py` for production.
- **Port Configuration:**
  - Backend: `8000`
  - Frontend: `3000`
- **API Endpoints:**
  - `GET /tasks/` - List all tasks
  - `POST /tasks/` - Create a new task
  - `PUT /tasks/{task_id}` - Update a task
  - `DELETE /tasks/{task_id}` - Delete a task

---

## Troubleshooting

- If you encounter issues with dependencies, ensure you are using the correct Node and Python versions.
- For CORS errors, make sure both frontend and backend are running and accessible at their respective ports.

---

## License

MIT License
