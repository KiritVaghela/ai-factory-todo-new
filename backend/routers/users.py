from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/users/register")
async def register_user(user: User):
    return {"username": user.username, "message": "User registered successfully!"}

@router.post("/users/login")
async def login_user(user: User):
    # Here you would normally implement login logic
    if user.username == "test" and user.password == "password":
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")