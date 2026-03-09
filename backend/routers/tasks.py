from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import sqlite3

router = APIRouter()

DATABASE = 'tasks.db'

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# Initialize the database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                          id INTEGER PRIMARY KEY,
                          title TEXT NOT NULL,
                          completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
                      );''')
    conn.close()

@router.post("/tasks/")
async def create_task(task: Task):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task.title, task.completed))
        task_id = cursor.lastrowid
        conn.commit()
        return {**task.dict(), "id": task_id}

@router.get("/tasks/")
async def get_tasks():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        return [{"id": task[0], "title": task[1], "completed": task[2]} for task in tasks]

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted successfully!"}

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE tasks SET title = ?, completed = ? WHERE id = ?', (task.title, task.completed, task_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return {**task.dict(), "id": task_id}

# Call the function to initialize the database when the module is loaded
init_db()