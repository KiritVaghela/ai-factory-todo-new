from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from routers import todos
import jwt
import os

app = FastAPI()

# JWT Middleware for validating tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.getenv('JWT_SECRET'), algorithms=['HS256'])
        return payload  # Here you can return the user object instead, if needed.
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid JWT token")

app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App API!"}

@app.get("/protected-route/")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": "This is a protected route!", "user": current_user}