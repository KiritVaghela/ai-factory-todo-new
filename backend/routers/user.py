from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from datetime import datetime, timedelta
import jwt

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = []
SECRET_KEY = "your_secret_key"  # Change this to a secure secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: Dict[str, str], expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/register/")
async def register_user(user: User):
    if any(u['username'] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db.append(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login/")
async def login_user(user: User):
    # This is a simple authentication step, ideally you should hash passwords
    for u in users_db:
        if u['username'] == user.username and u['password'] == user.password:
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
            return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")