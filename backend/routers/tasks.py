from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

tasks = []

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

@router.post("/tasks/")
async def create_task(task: Task, token: str = Depends(oauth2_scheme)):
    tasks.append(task)
    return task

@router.get("/tasks/")
async def get_tasks(token: str = Depends(oauth2_scheme)):
    return tasks

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, token: str = Depends(oauth2_scheme)):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted successfully!"}