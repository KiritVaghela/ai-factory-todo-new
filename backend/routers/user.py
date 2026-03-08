from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import datetime

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

users_db = []
SECRET_KEY = "your_secret_key"

@router.post("/register/")
async def register_user(user: User):
    if any(u['username'] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db.append(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login/", response_model=Token)
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = next((u for u in users_db if u['username'] == form_data.username), None)
    if not user or form_data.password != user['password']:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    token = jwt.encode({
        "sub": user['username'],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}