from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = []
tokens_db = {}  # Simple in-memory token store

@router.post("/register/")
async def register_user(user: User):
    if any(u['username'] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db.append(user.dict())
    return {"message": "User registered successfully"}

@router.post("/token")
async def login(user: User):
    if not any(u['username'] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = f"token_for_{user.username}"
    tokens_db[token] = user.username  # Store token
    return {"access_token": token, "token_type": "bearer"}