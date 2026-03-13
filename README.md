# ToDo App

This is a full-stack ToDo application built with:

- Frontend: React + Vite + TailwindCSS
- Backend: FastAPI + SQLite

## Development Setup

### Frontend

1. Navigate to `frontend` directory
2. Run `npm install`
3. Run `npm run dev`

### Backend

1. Navigate to `backend` directory
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run server: `python main.py`

## Docker Setup

1. Build containers: `docker-compose build`
2. Start services: `docker-compose up`
3. Verify containers:
   - Frontend: http://localhost:3000
   - Backend: http://localhost:8000

To stop containers: `docker-compose down`

## Testing

### Frontend

Run tests: `npm test`

### Backend

Run tests: `pytest`
