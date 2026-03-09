from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter()

# Database connection setup
DATABASE = 'tasks.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enable accessing columns by name
    return conn

@router.options("/tasks")
async def options_tasks():
    return {
        "message": "CORS options for /tasks",
        "allowed_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    }

@router.get("/tasks/")
async def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return [dict(task) for task in tasks]

@router.post("/tasks/")
async def create_task(task: dict):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task['title'], task['completed']))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()  
    return {"id": task_id, "title": task['title'], "completed": task['completed']}

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: dict):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET title = ?, completed = ? WHERE id = ?', (task['title'], task['completed'], task_id))
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    conn.close()
    return {"id": task_id, "title": task['title'], "completed": task['completed']}

@router.put("/tasks/{task_id}/complete")
async def complete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', (True, task_id))
    if cursor.rowcount == 0:
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
        raise HTTPException(status_code=404, detail="Task not found")
    conn.commit()
    conn.close()
    return {"message": "Task deleted successfully"}
