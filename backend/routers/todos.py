from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

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
async def create_todo(item: TodoItem, user: str = Depends(get_current_user)):
    todos.append(item)
    return item

@router.put("/todos/{id}")
async def update_todo(id: int, item: TodoItem, user: str = Depends(get_current_user)):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{id}")
async def delete_todo(id: int, user: str = Depends(get_current_user)):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(idx)
            return {"detail": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")