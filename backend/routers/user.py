from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
import jwt
import datetime

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = []

SECRET_KEY = "your_secret_key"

@router.post("/register/")
async def register_user(user: User):
    if any(u['username'] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db.append(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login/")
async def login_user(user: User) -> Dict[str, str]:
    for u in users_db:
        if u['username'] == user.username and u['password'] == user.password:
            token = jwt.encode({"sub": user.username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY, algorithm="HS256")
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")