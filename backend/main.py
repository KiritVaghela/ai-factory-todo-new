from fastapi import FastAPI
from routers import tasks
from fastapi.testclient import TestClient

app = FastAPI()

app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the ToDo App API"}


# Test the application to ensure that the updated version of FastAPI works without breaking existing functionality.
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ToDo App API"}


def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "completed": False})
    assert response.status_code == 200
    assert response.json()['title'] == "Test Task"


def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_task():
    # First, create a task to update
    resp = client.post("/tasks/", json={"title": "Task to update", "completed": False})
    task_id = resp.json()['id']
    update_response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "completed": True})
    assert update_response.status_code == 200
    assert update_response.json()['title'] == "Updated Task"
    assert update_response.json()['completed'] is True


def test_delete_task():
    # First, create a task to delete
    resp = client.post("/tasks/", json={"title": "Task to delete", "completed": False})
    task_id = resp.json()['id']
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()['message'] == "Task deleted successfully!"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
