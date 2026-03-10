from fastapi import FastAPI
from routers import tasks
from starlette.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
import subprocess
import sys

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for your application
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

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
    assert delete_response.json()['message'] == "Task deleted successfully"


def run_lint_and_tests():
    """
    Run backend linting and tests to ensure no regressions and code quality.
    """
    print("Running linting with flake8...")
    lint_result = subprocess.run([sys.executable, '-m', 'flake8', '.'], capture_output=True, text=True)
    if lint_result.returncode != 0:
        print("Linting errors found:")
        print(lint_result.stdout)
        print(lint_result.stderr)
        raise Exception("Linting failed")
    else:
        print("No linting errors found.")

    print("Running tests with pytest...")
    test_result = subprocess.run([sys.executable, '-m', 'pytest', '--maxfail=1', '--disable-warnings', '-q'], capture_output=True, text=True)
    print(test_result.stdout)
    if test_result.returncode != 0:
        print("Tests failed:")
        print(test_result.stderr)
        raise Exception("Tests failed")
    else:
        print("All tests passed successfully.")


if __name__ == "__main__":
    # Run lint and tests when this script is executed directly
    run_lint_and_tests()
