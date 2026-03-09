from fastapi import FastAPI
from routers import tasks, users

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the ToDo App API"}