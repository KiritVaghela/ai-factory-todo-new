import jwt
import datetime
from typing import Dict, Any

# Secret key for encoding and decoding the JWT
SECRET_KEY = "your_secret_key_here"

# Function to generate a new JWT token
def create_jwt_token(data: Dict[str, Any], expires_minutes: int = 30) -> str:
    expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_minutes)
    data['exp'] = expiration
    token = jwt.encode(data, SECRET_KEY, algorithm="HS256")
    return token

# Function to decode and verify a JWT token
def decode_jwt_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")