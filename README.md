# ToDo App - AI Factory

This is a full-stack ToDo application with a FastAPI backend and a React (Vite + Tailwind CSS) frontend. It is containerized using Docker and orchestrated with docker-compose for easy development and deployment.

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
    README.md
    vite.config.js
    index.css
    index.html
    tailwind.config.js
    package.json
    package-lock.json
    babel.config.js
    index.jsx
    install-dependencies.js
    src/
      main.jsx
      styles.css
      DeleteButton.jsx
      App.jsx
      TaskList.jsx
```

## Prerequisites

- [Docker](https://www.docker.com/) and [docker-compose](https://docs.docker.com/compose/) installed
- (For local development) [Python 3.11+](https://www.python.org/) and [Node.js 18+](https://nodejs.org/)

---

## Quick Start (Recommended: Docker Compose)

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd ai-factory-todo-new
   ```

2. **Build and start all services:**
   ```bash
   docker-compose up --build
   ```
   - The backend will be available at [http://localhost:8000](http://localhost:8000)
   - The frontend will be available at [http://localhost:3000](http://localhost:3000)

3. **Stop services:**
   ```bash
   docker-compose down
   ```

---

## Manual Setup (Local Development)

### Backend (FastAPI)

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

3. **Run the backend server:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   - API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Frontend (React + Vite + Tailwind CSS)

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```
   - App will be available at [http://localhost:3000](http://localhost:3000)

---

## Environment Variables

- Backend uses `.env` file (see `backend/.env.example` for template).
- For development, default settings should work out of the box.

---

## Running Tests

- **Backend:** (if tests are present)
  ```bash
  cd backend
  # pytest or other test runner
  ```
- **Frontend:**
  ```bash
  cd frontend
  npm test
  ```

---

## Linting

- **Backend:**
  ```bash
  cd backend
  # Example: flake8 main.py
  ```
- **Frontend:**
  ```bash
  cd frontend
  npm run lint
  ```

---

## Troubleshooting

- If you change dependencies, rebuild Docker images: `docker-compose build --no-cache`
- If ports are in use, stop other services or change the ports in `docker-compose.yml` and `vite.config.js`.
- For CORS issues, ensure backend allows requests from frontend origin (see FastAPI CORS middleware in `backend/main.py`).

---

## License

MIT
