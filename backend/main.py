from fastapi import FastAPI, Depends, HTTPException
from routers import todo_router, user_router
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# Authentication middleware
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def fake_decode_token(token):
    # Fake decoding logic - to be replaced with real logic
    return "user"

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    return user

@app.get("/")
async def read_root(current_user: str = Depends(get_current_user)):
    return {"message": "Welcome to the Todo API"}

app.include_router(todo_router)
app.include_router(user_router)