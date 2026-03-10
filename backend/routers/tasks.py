import sqlite3
from typing import Any, Dict

from fastapi import APIRouter, Body, HTTPException, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os

router = APIRouter()

# Database connection setup
DATABASE = "backend/tasks.db"

# JWT secret and algorithm (should be set in environment in production)
JWT_SECRET = os.getenv("JWT_SECRET", "your_jwt_secret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

# HTTPBearer for extracting the Authorization header
bearer_scheme = HTTPBearer()

def verify_jwt(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> dict:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable accessing columns by name
    return conn


@router.options("/tasks/")
async def options_tasks():
    return {
        "message": "CORS options for /tasks",
        "allowed_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    }


@router.get("/tasks/")
async def get_tasks(user: dict = Depends(verify_jwt)):
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [dict(task) for task in tasks]


@router.post("/tasks/")
async def create_task(task: Dict[str, Any] = Body(...), user: dict = Depends(verify_jwt)):
    if "title" not in task or "completed" not in task:
        raise HTTPException(
            status_code=422, detail="Missing 'title' or 'completed' in request body"
        )
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, completed) VALUES (?, ?)",
        (task["title"], int(task["completed"])),
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, "title": task["title"], "completed": task["completed"]}


@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Dict[str, Any] = Body(...), user: dict = Depends(verify_jwt)):
    if "title" not in task or "completed" not in task:
        raise HTTPException(
            status_code=422, detail="Missing 'title' or 'completed' in request body"
        )
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, completed = ? WHERE id = ?",
        (task["title"], int(task["completed"]), task_id),
    )
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    conn.close()
    return {"id": task_id, "title": task["title"], "completed": task["completed"]}


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, user: dict = Depends(verify_jwt)):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    conn.close()
    return {"message": f"Task {task_id} deleted"}
