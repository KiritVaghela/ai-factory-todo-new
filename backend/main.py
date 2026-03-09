from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routers import todos, user
from typing import List
from datetime import datetime, timedelta
from jose import JWTError, jwt

# JWT SECRET KEY AND ALGORITHM
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implement your user authentication logic here
    pass

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Implement JWT validation logic here
    pass

app.include_router(todos.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App API!"}