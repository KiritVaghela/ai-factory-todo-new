from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

tasks = []

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

@router.post("/tasks/")
async def create_task(task: Task):
    tasks.append(task)
    return task

@router.get("/tasks/")
async def get_tasks():
    return tasks

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    return {"message": "Task deleted successfully!"}