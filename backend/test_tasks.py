import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

# Helper function to create a task

def create_task(title="Test Task", completed=False):
    response = client.post("/tasks/", json={"title": title, "completed": completed})
    assert response.status_code == 200
    return response.json()

# Test getting tasks returns a list

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test creating a task

def test_create_task():
    task_data = {"title": "New Task", "completed": False}
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == task_data["title"]
    assert data["completed"] == task_data["completed"]
    assert "id" in data

# Test updating a task

def test_update_task():
    task = create_task("Task to update", False)
    task_id = task["id"]
    update_data = {"title": "Updated Task", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_data["title"]
    assert data["completed"] == update_data["completed"]

# Test updating a non-existent task returns 404

def test_update_nonexistent_task():
    update_data = {"title": "Nonexistent Task", "completed": True}
    response = client.put("/tasks/999999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

# Test completing a task

def test_complete_task():
    task = create_task("Task to complete", False)
    task_id = task["id"]
    response = client.put(f"/tasks/{task_id}/complete")
    assert response.status_code == 200
    assert response.json()["message"] == "Task marked as completed"

# Test completing a non-existent task returns 404

def test_complete_nonexistent_task():
    response = client.put("/tasks/999999/complete")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

# Test deleting a task

def test_delete_task():
    task = create_task("Task to delete", False)
    task_id = task["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

# Test deleting a non-existent task returns 404

def test_delete_nonexistent_task():
    response = client.delete("/tasks/999999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
