from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import datetime

router = APIRouter()

class User(BaseModel):
    username: str
    email: str
    password: str

users_db = []

# JWT Secret Key
SECRET_KEY = "your_secret_key"

# JWT Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def create_jwt_token(data: dict):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    token = jwt.encode({**data, 'exp': expiration_time}, SECRET_KEY, algorithm="HS256")
    return token

@router.post("/register/")
async def register_user(user: User):
    if any(u['username'] == user.username for u in users_db):
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db.append(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login/")
async def login(user: OAuth2PasswordRequestForm = Depends()):
    for db_user in users_db:
        if db_user['username'] == user.username and db_user['password'] == user.password:
            token = create_jwt_token({'sub': user.username})
            return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")