import jwt
import datetime
from typing import Dict, Any

# Secret key for encoding and decoding JWT tokens
SECRET_KEY = "your_secret_key"

def encode_jwt(data: Dict[str, Any], expires_delta: datetime.timedelta = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt


def decode_jwt(token: str) -> Dict[str, Any]:
    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}