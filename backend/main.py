from fastapi import FastAPI
from routers import tasks, users, todos
from fastapi.testclient import TestClient

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(todos.router)  # Added todos router

@app.get("/")
async def root():
    return {"message": "Welcome to the ToDo App API"}


# Test the application to ensure that the updated version of FastAPI works without breaking existing functionality.
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ToDo App API"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
