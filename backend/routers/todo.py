from fastapi import APIRouter, HTTPException, Depends
from models import Todo
from typing import List
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
todos_db = []

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user

@router.post("/todos/", response_model=Todo)
async def create_todo(todo: Todo, current_user: str = Depends(get_current_user)):
    todos_db.append(todo)
    return todo

@router.get("/todos/", response_model=List[Todo])
async def read_todos(current_user: str = Depends(get_current_user)):
    return todos_db