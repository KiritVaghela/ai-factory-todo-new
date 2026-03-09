from fastapi import APIRouter, HTTPException
from models import Todo
from typing import List
import sqlite3

router = APIRouter()

DATABASE = 'todos.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@router.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (title, completed) VALUES (?, ?)", (todo.title, todo.completed))
    conn.commit()
    conn.close()
    return todo

@router.get("/todos/", response_model=List[Todo])
async def read_todos():
    conn = get_db_connection()
    todos = conn.execute("SELECT * FROM todos").fetchall()
    conn.close()
    return [dict(todo) for todo in todos]

@router.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: Todo):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET title = ?, completed = ? WHERE id = ?", (todo.title, todo.completed, todo_id))
    conn.commit()
    conn.close()
    return todo

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return {"message": "Todo deleted successfully!"}
