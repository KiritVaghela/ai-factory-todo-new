from fastapi import FastAPI
from routers import todos, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update as per your requirements
    allow_credentials=True,
    allow_methods=["*"] ,
    allow_headers=["*"]
)

app.include_router(todos.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App API!"}