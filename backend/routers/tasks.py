from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.options("/tasks")
async def options_tasks():
    return {
        "message": "CORS options for /tasks",
        "allowed_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    }

@router.get("/tasks/")
async def get_tasks():
    # Logic to retrieve tasks
    pass

@router.post("/tasks/")
async def create_task(task: dict):
    # Logic to create a task
    pass

@router.put("/tasks/{task_id}")
async def update_task(task_id: int, task: dict):
    # Logic to update a task
    pass

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    # Logic to delete a task
    pass
