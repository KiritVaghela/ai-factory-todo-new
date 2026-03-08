from fastapi import FastAPI, Depends
from routers import todos, user
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# Authentication Middleware
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def authenticate(token: str = Depends(oauth2_scheme)):
    # Here you would validate the token in a real application
    return token

app.include_router(todos.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App API!"}