from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        token = request.headers.get("Authorization")
        if not token or token != "Bearer your_token_here":  # Replace with real token validation
            raise HTTPException(status_code=403, detail="Not authenticated")
        response = await call_next(request)
        return response