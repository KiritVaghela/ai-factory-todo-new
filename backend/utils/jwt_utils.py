from datetime import datetime, timedelta
import jwt
from typing import Dict, Any

class JWTHandler:
    SECRET_KEY = "your_secret_key"
    ALGORITHM = "HS256"
    EXPIRATION_DELTA = timedelta(days=1)

    @staticmethod
    def create_token(data: Dict[str, Any]) -> str:
        data['exp'] = datetime.utcnow() + JWTHandler.EXPIRATION_DELTA
        return jwt.encode(data, JWTHandler.SECRET_KEY, algorithm=JWTHandler.ALGORITHM)

    @staticmethod
    def verify_token(token: str) -> Dict[str, Any]:
        try:
            payload = jwt.decode(token, JWTHandler.SECRET_KEY, algorithms=[JWTHandler.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise Exception("Token has expired")
        except jwt.InvalidTokenError:
            raise Exception("Invalid token")