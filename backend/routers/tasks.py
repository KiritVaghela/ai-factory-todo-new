from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import sqlite3
from typing import List

router = APIRouter()

# Database connection setup
DATABASE = 'tasks.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable accessing columns by name
    return conn

class Task(BaseModel):
    title: str
    completed: bool

class TaskResponse(Task):
    id: int

@router.options("/tasks/")
async def options_tasks():
    return {
        "message": "CORS options for /tasks",
        "allowed_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    }

@router.get("/tasks/", response_model=List[TaskResponse])
async def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return [dict(task) for task in tasks]

@router.post("/tasks/", response_model=TaskResponse)
async def create_task(task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task.title, int(task.completed)))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, "title": task.title, "completed": task.completed}

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(task_id: int, task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET title = ?, completed = ? WHERE id = ?', (task.title, int(task.completed), task_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    conn.close()
    return {"id": task_id, "title": task.title, "completed": task.completed}

@router.put("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (1, task_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    conn.close()
    return {"message": "Task marked as completed"}

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    conn.close()
    return {"message": "Task deleted successfully"}
