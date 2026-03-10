import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from main import app

client = TestClient(app)

# Helper function to simulate database connection error
class DummyConnectionError(Exception):
    pass

# Test error handling for GET /tasks/
@patch('routers.tasks.get_db_connection')
def test_get_tasks_db_error(mock_get_db_connection):
    # Simulate database connection error
    mock_get_db_connection.side_effect = DummyConnectionError("DB connection failed")

    response = client.get("/tasks/")
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

# Test error handling for POST /tasks/
@patch('routers.tasks.get_db_connection')
def test_create_task_db_error(mock_get_db_connection):
    mock_get_db_connection.side_effect = DummyConnectionError("DB connection failed")

    response = client.post("/tasks/", json={"title": "Test Task", "completed": False})
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

# Test error handling for PUT /tasks/{task_id}
@patch('routers.tasks.get_db_connection')
def test_update_task_db_error(mock_get_db_connection):
    mock_get_db_connection.side_effect = DummyConnectionError("DB connection failed")

    response = client.put("/tasks/1", json={"title": "Updated Task", "completed": True})
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

# Test error handling for DELETE /tasks/{task_id}
@patch('routers.tasks.get_db_connection')
def test_delete_task_db_error(mock_get_db_connection):
    mock_get_db_connection.side_effect = DummyConnectionError("DB connection failed")

    response = client.delete("/tasks/1")
    assert response.status_code == 500
    assert response.json() == {"detail": "Database connection error"}

# Test error handling for invalid task update (task not found)
@patch('routers.tasks.get_db_connection')
def test_update_task_not_found(mock_get_db_connection):
    # Setup mock connection and cursor
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Simulate no rows updated
    mock_cursor.rowcount = 0

    response = client.put("/tasks/9999", json={"title": "Nonexistent Task", "completed": True})
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

# Test error handling for invalid task delete (task not found)
@patch('routers.tasks.get_db_connection')
def test_delete_task_not_found(mock_get_db_connection):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_get_db_connection.return_value = mock_conn
    mock_conn.cursor.return_value = mock_cursor

    # Simulate no rows deleted
    mock_cursor.rowcount = 0

    response = client.delete("/tasks/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}
