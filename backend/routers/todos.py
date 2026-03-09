from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import JWTBearer, OAuth2PasswordBearer

router = APIRouter()
todos = []  # This will act as an in-memory database

token_auth_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def get_current_user(token: str = Depends(token_auth_scheme)):
    # Here, you would implement your JWT decoding and validation logic
    return True  # Placeholder return value; replace with actual user checking

class TodoItem(BaseModel):
    id: int
    title: str
    completed: bool = False

@router.get("/todos", dependencies=[Depends(get_current_user)])
def read_todos():
    return todos

@router.post("/todos", dependencies=[Depends(get_current_user)])
def create_todo(item: TodoItem):
    todos.append(item)
    return item

@router.put("/todos/{id}", dependencies=[Depends(get_current_user)])
def update_todo(id: int, item: TodoItem):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos[idx] = item
            return item
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todos/{id}", dependencies=[Depends(get_current_user)])
def delete_todo(id: int):
    for idx, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(idx)
            return {"detail": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")