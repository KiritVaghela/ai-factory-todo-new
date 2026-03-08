from fastapi import APIRouter, HTTPException, Depends
from models import Todo
from typing import List
from main import get_current_user

router = APIRouter()
todos_db = []

@router.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo, current_user: str = Depends(get_current_user)):
    todos_db.append(todo)
    return todo

@router.get("/todos/", response_model=List[Todo])
async def read_todos(current_user: str = Depends(get_current_user)):
    return todos_db