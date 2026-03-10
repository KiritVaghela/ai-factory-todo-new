# Backend - ToDo App

This directory contains the backend code for the ToDo App, built with FastAPI and SQLite.

## Table of Contents
- [Setup](#setup)
- [Running the Backend](#running-the-backend)
- [Database](#database)
- [API Endpoints](#api-endpoints)
- [JWT Authentication](#jwt-authentication)
- [Environment Variables](#environment-variables)

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

   Copy `.env.example` to `.env` and update values as needed.

   ```bash
   cp .env.example .env
   ```

---

## Running the Backend

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000/`.

---

## Database

- Uses SQLite (`tasks.db` by default).
- The schema is created by `db_setup.py`.

---

## API Endpoints

- `GET    /tasks/`         - List all tasks
- `POST   /tasks/`         - Create a new task
- `PUT    /tasks/{id}`     - Update a task
- `DELETE /tasks/{id}`     - Delete a task

---

## JWT Authentication

The backend supports JWT (JSON Web Token) authentication for securing API endpoints.

### How JWT Authentication Works

1. **Login:**
   - The client sends credentials (e.g., username and password) to a login endpoint (e.g., `/auth/login`).
   - If valid, the backend returns a JWT access token.

2. **Accessing Protected Endpoints:**
   - The client includes the JWT token in the `Authorization` header for requests to protected endpoints:
     
     ```http
     Authorization: Bearer <your_jwt_token>
     ```

3. **Token Verification:**
   - The backend verifies the token's signature and validity before allowing access.

### Example Usage

#### 1. Obtain a JWT Token

```bash
curl -X POST http://localhost:8000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username": "your_username", "password": "your_password"}'
```

**Response:**
```json
{
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

#### 2. Access a Protected Endpoint

```bash
curl -X GET http://localhost:8000/tasks/ \
     -H "Authorization: Bearer <JWT_TOKEN>"
```

### Configuration

- The JWT secret key and algorithm are set in the `.env` file:

  ```env
  JWT_SECRET_KEY=your_secret_key
  JWT_ALGORITHM=HS256
  JWT_ACCESS_TOKEN_EXPIRE_MINUTES=30
  ```

- Make sure to keep your secret key safe and never commit it to version control.

### Implementation Notes

- The backend uses the `python-jose` and `passlib` libraries for JWT and password hashing.
- You may need to implement or update the `/auth/login` endpoint and user management as needed.
- Protect endpoints by requiring authentication using FastAPI's `Depends` and OAuth2PasswordBearer.

---

## Environment Variables

See `.env.example` for all available environment variables and their descriptions.
