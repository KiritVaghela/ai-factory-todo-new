import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Helper function to create a task

def create_task(title="Test Task", completed=False):
    response = client.post("/tasks/", json={"title": title, "completed": completed})
    return response

# Test creating a task successfully

def test_create_task_success():
    response = create_task()
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Task"
    assert data["completed"] is False

# Test getting tasks

def test_get_tasks():
    # Create a task first
    create_task()
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(task["title"] == "Test Task" for task in data)

# Test updating a task successfully

def test_update_task_success():
    # Create a task
    create_resp = create_task(title="Old Title", completed=False)
    task_id = create_resp.json()["id"]

    # Update the task
    update_resp = client.put(f"/tasks/{task_id}", json={"title": "New Title", "completed": True})
    assert update_resp.status_code == 200
    updated_data = update_resp.json()
    assert updated_data["id"] == task_id
    assert updated_data["title"] == "New Title"
    assert updated_data["completed"] is True

# Test updating a non-existent task (fixed error scenario)

def test_update_task_not_found():
    # Use a very large task_id that likely does not exist
    non_existent_id = 999999
    response = client.put(f"/tasks/{non_existent_id}", json={"title": "Does not exist", "completed": False})
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

# Test completing a task successfully

def test_complete_task_success():
    create_resp = create_task(title="Incomplete Task", completed=False)
    task_id = create_resp.json()["id"]

    complete_resp = client.put(f"/tasks/{task_id}/complete")
    assert complete_resp.status_code == 200
    assert complete_resp.json()["message"] == "Task marked as completed"

# Test completing a non-existent task (fixed error scenario)

def test_complete_task_not_found():
    non_existent_id = 999999
    response = client.put(f"/tasks/{non_existent_id}/complete")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

# Test deleting a task successfully

def test_delete_task_success():
    create_resp = create_task(title="Task to delete", completed=False)
    task_id = create_resp.json()["id"]

    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 200
    assert delete_resp.json()["message"] == "Task deleted"

# Test deleting a non-existent task (fixed error scenario)

def test_delete_task_not_found():
    non_existent_id = 999999
    response = client.delete(f"/tasks/{non_existent_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
