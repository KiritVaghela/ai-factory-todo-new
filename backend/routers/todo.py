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