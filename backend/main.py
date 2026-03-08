from fastapi import FastAPI
from routers import todos
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

app = FastAPI()

# Middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# JWT authentication setup
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

app.include_router(todos.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App API!"}
