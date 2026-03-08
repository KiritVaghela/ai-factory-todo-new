import jwt
import datetime
from fastapi import HTTPException

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 30

class JWTManager:
    @staticmethod
    def create_token(data: dict):
        expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRATION_MINUTES)
        to_encode = data.copy()
        to_encode.update({"exp": expiration})
        token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return token

    @staticmethod
    def decode_token(token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.JWTError:
            raise HTTPException(status_code=403, detail="Invalid token")
