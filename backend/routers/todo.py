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