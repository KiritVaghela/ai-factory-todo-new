from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task():
    task_data = {"title": "Test Task", "completed": False}
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["completed"] is False


def test_update_task():
    # First create a task
    task_data = {"title": "Test Task", "completed": False}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    # Update the task
    updated_data = {"title": "Updated Task", "completed": True}
    update_response = client.put(f"/tasks/{task_id}", json=updated_data)
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Task"
    assert update_response.json()["completed"] is True


def test_delete_task():
    # First create a task
    task_data = {"title": "Test Task", "completed": False}
    create_response = client.post("/tasks/", json=task_data)
    task_id = create_response.json()["id"]

    # Delete the task
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 200

    # Verify task is deleted
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


def test_invalid_task_creation():
    invalid_data = {"title": ""}  # Missing completed field
    response = client.post("/tasks/", json=invalid_data)
    assert response.status_code == 422


def test_update_nonexistent_task():
    updated_data = {"title": "Updated Task", "completed": True}
    response = client.put("/tasks/999999", json=updated_data)
    assert response.status_code == 404


def test_delete_nonexistent_task():
    response = client.delete("/tasks/999999")
    assert response.status_code == 404
