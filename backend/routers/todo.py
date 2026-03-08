from fastapi import APIRouter, HTTPException, Depends
from models import Todo
from typing import List
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
todos_db = []

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def verify_token(token: str = Depends(oauth2_scheme)):  # Function to verify JWT token
    # Implement your JWT verification logic here
    # For demo purposes, we assume the token is valid if it's a non-empty string
    if token != '':
        return True
    raise HTTPException(status_code=403, detail="Unauthorized")

@router.post("/todos/", response_model=Todo, dependencies=[Depends(verify_token)])  # Protect route with token check
async def create_todo(todo: Todo):
    todos_db.append(todo)
    return todo

@router.get("/todos/", response_model=List[Todo], dependencies=[Depends(verify_token)])  # Protect route with token check
async def read_todos():
    return todos_db