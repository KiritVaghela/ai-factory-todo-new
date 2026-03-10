# Backend - ToDo App

This is the backend for the ToDo App, built with FastAPI and SQLite.

## Table of Contents
- [Setup](#setup)
- [Running the Server](#running-the-server)
- [Environment Variables](#environment-variables)
- [Database](#database)
- [API Endpoints](#api-endpoints)
- [JWT Authentication](#jwt-authentication)
- [CORS](#cors)

---

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up the database:**
   ```bash
   python db_setup.py
   ```

3. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in the required values.

## Running the Server

Start the FastAPI server:
```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000/`.

## Environment Variables

See `.env.example` for required environment variables. If using JWT authentication, you must set a secret key:

```
JWT_SECRET=your_secret_key_here
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=60
```

## Database

The backend uses SQLite. The default database file is `tasks.db` in the `backend/` directory.

## API Endpoints

- `GET /tasks/` - List all tasks
- `POST /tasks/` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## JWT Authentication

Some endpoints may require JWT authentication. Here is how to use JWT with this backend:

### 1. Obtain a JWT Token

You must authenticate (e.g., via a `/login` endpoint, if implemented) to receive a JWT token. The backend will return a token like:

```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### 2. Use the JWT Token in Requests

For endpoints that require authentication, include the JWT token in the `Authorization` header:

```
Authorization: Bearer <JWT_TOKEN>
```

**Example using `curl`:**

```bash
curl -H "Authorization: Bearer <JWT_TOKEN>" http://localhost:8000/tasks/
```

### 3. Token Verification

The backend will verify the JWT token using the secret and algorithm specified in your `.env` file. If the token is invalid or expired, the API will return a 401 Unauthorized error.

### 4. Customizing JWT Settings

You can adjust the following environment variables in your `.env` file:
- `JWT_SECRET`: Secret key for signing tokens
- `JWT_ALGORITHM`: Algorithm used (default: HS256)
- `JWT_EXPIRATION_MINUTES`: Token expiration time in minutes

### 5. Example Python Usage

```python
import requests

jwt_token = "<JWT_TOKEN>"
headers = {"Authorization": f"Bearer {jwt_token}"}
response = requests.get("http://localhost:8000/tasks/", headers=headers)
print(response.json())
```

### 6. Notes
- If JWT authentication is not enabled, you can access endpoints without a token.
- If you add authentication to endpoints, update your frontend to include the JWT token in requests.

## CORS

CORS is enabled for all origins by default. Adjust `allow_origins` in `main.py` as needed for production.

---

For more details, see the code and comments in `main.py` and `routers/tasks.py`.
