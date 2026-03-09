from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

todos = []  # This will act as an in-memory database

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Here you would verify the token and return the user
    pass  # Implement token verification logic

@router.get("/todos")
def read_todos(current_user: str = Depends(get_current_user)):
    return todos

@router.post("/todos")
def create_todo(item: TodoItem, current_user: str = Depends(get_current_user)):
    todos.append(item)
    return item

@router.put("/todos/{id}")
def update_todo(id: int, item: TodoItem, current_user: str = Depends(get_current_user)):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{id}")
def delete_todo(id: int, current_user: str = Depends(get_current_user)):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(idx)
            return {"detail": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")