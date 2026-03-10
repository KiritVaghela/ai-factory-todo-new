from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
import sqlite3
import logging

router = APIRouter()

# Configure logger
logger = logging.getLogger(__name__)

# Database connection setup
DATABASE = 'tasks.db'

def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row  # Enable accessing columns by name
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")

# Define Pydantic models for request validation
class Task(BaseModel):
    title: str
    completed: bool

class TaskUpdate(Task):
    pass

@router.options("/tasks")
async def options_tasks():
    return {
        "message": "CORS options for /tasks",
        "allowed_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    }

@router.get("/tasks/")
async def get_tasks():
    try:
        conn = get_db_connection()
        tasks = conn.execute('SELECT * FROM tasks').fetchall()
        conn.close()
        return [dict(task) for task in tasks]
    except sqlite3.Error as e:
        logger.error(f"Error fetching tasks: {e}")
        raise HTTPException(status_code=500, detail="Error fetching tasks")

@router.post("/tasks/")
async def create_task(task: Task):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task.title, task.completed))
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return {"id": task_id, "title": task.title, "completed": task.completed}
    except sqlite3.Error as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Error creating task")

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: TaskUpdate):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        existing_task = cursor.fetchone()
        if existing_task is None:
            conn.close()
            logger.warning(f"Task with id {task_id} not found for update")
            raise HTTPException(status_code=404, detail="Task not found")

        cursor.execute('UPDATE tasks SET title = ?, completed = ? WHERE id = ?', (task.title, task.completed, task_id))
        conn.commit()
        conn.close()
        return {"id": task_id, "title": task.title, "completed": task.completed}
    except sqlite3.Error as e:
        logger.error(f"Error updating task {task_id}: {e}")
        raise HTTPException(status_code=500, detail="Error updating task")

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        existing_task = cursor.fetchone()
        if existing_task is None:
            conn.close()
            logger.warning(f"Task with id {task_id} not found for deletion")
            raise HTTPException(status_code=404, detail="Task not found")

        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
        return {"message": f"Task {task_id} deleted successfully"}
    except sqlite3.Error as e:
        logger.error(f"Error deleting task {task_id}: {e}")
        raise HTTPException(status_code=500, detail="Error deleting task")
