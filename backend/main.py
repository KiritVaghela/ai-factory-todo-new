from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import tasks, users
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  # Allow all origins for this example
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def verify_token(token: str = Depends(oauth2_scheme)):
    # Placeholder for token verification logic
    if token != "valid_token":  # Replace with actual verification process
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the ToDo App API"}