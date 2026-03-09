from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()

# Define the task model
class Task(BaseModel):
    id: int
    title: str
    completed: bool

# Mock database
tasks_db = []

@router.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    tasks_db.append(task)
    return task

@router.get("/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks_db

@router.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    global tasks_db
    # Find the task
    task_to_delete = next((task for task in tasks_db if task.id == task_id), None)
    if not task_to_delete:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_db.remove(task_to_delete)
    return {"message": "Task deleted successfully!"}
