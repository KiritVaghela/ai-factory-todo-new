from fastapi import APIRouter, HTTPException
from models import Todo
from typing import List

router = APIRouter()
todos_db = []

@router.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo):
    todos_db.append(todo)
    return todo

@router.get("/todos/", response_model=List[Todo])
async def read_todos():
    return todos_db

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    global todos_db
    todos_db = [todo for todo in todos_db if todo.id != todo_id]
    return {"message": "Todo deleted successfully!"}

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    global todos_db
    todos_db = [todo for todo in todos_db if todo.id != task_id]
    return {"message": "Task deleted successfully!"}