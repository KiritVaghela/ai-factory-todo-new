from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

todos = []  # This will act as an in-memory database

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

@router.get("/todos")
def read_todos():
    return todos

@router.post("/todos")
def create_todo(item: TodoItem):
    todos.append(item)
    return item

@router.put("/todos/{id}")
def update_todo(id: int, item: TodoItem):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{id}")
def delete_todo(id: int):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(idx)
            return {"detail": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")