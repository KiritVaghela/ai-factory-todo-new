from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routers import tasks

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the ToDo App API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
