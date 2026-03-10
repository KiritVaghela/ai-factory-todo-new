from fastapi import FastAPI, Request
from routers import tasks
from starlette.middleware.cors import CORSMiddleware
from fastapi.testclient import TestClient
import logging
import uvicorn

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for your application
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(tasks.router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    try:
        response = await call_next(request)
        logger.info(f"Response status: {response.status_code} for {request.method} {request.url}")
        return response
    except Exception as e:
        logger.error(f"Unhandled error during request {request.method} {request.url}: {e}", exc_info=True)
        raise

@app.get("/")
async def root():
    logger.debug("Root endpoint called")
    return {"message": "Welcome to the ToDo App API"}

# Test the application to ensure that the updated version of FastAPI works without breaking existing functionality.
client = TestClient(app)

def test_root():
    logger.debug("Testing root endpoint")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ToDo App API"}


def test_create_task():
    logger.debug("Testing create task endpoint")
    response = client.post("/tasks/", json={"title": "Test Task", "completed": False})
    assert response.status_code == 200
    assert response.json()['title'] == "Test Task"


def test_get_tasks():
    logger.debug("Testing get tasks endpoint")
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_task():
    logger.debug("Testing update task endpoint")
    # First, create a task to update
    resp = client.post("/tasks/", json={"title": "Task to update", "completed": False})
    task_id = resp.json()['id']
    update_response = client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "completed": True})
    assert update_response.status_code == 200
    assert update_response.json()['title'] == "Updated Task"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
