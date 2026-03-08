from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = []

@router.post("/register/")
async def register_user(user: User):
    if any(u['username'] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db.append(user.dict())
    return {"message": "User registered successfully"}