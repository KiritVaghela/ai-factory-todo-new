import jwt
import datetime
from typing import Any, Dict, Optional

# You should set this secret key securely in production, e.g., from environment variables
JWT_SECRET = "your-secret-key"  # Replace with a secure value or load from env
JWT_ALGORITHM = "HS256"


def encode_jwt(payload: Dict[str, Any], expires_delta: Optional[datetime.timedelta] = None) -> str:
    """
    Encode a JWT token with the given payload and optional expiration delta.
    :param payload: The payload to encode in the JWT.
    :param expires_delta: Optional timedelta for token expiration.
    :return: Encoded JWT as a string.
    """
    payload_to_encode = payload.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
        payload_to_encode["exp"] = expire
    return jwt.encode(payload_to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_jwt(token: str) -> Dict[str, Any]:
    """
    Decode a JWT token and return the payload.
    :param token: JWT token as a string.
    :return: Decoded payload as a dict.
    :raises jwt.ExpiredSignatureError: If the token is expired.
    :raises jwt.InvalidTokenError: If the token is invalid.
    """
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])


# Example usage (remove or comment out in production):
if __name__ == "__main__":
    data = {"user_id": 123, "username": "alice"}
    token = encode_jwt(data, expires_delta=datetime.timedelta(minutes=15))
    print("Encoded JWT:", token)
    decoded = decode_jwt(token)
    print("Decoded JWT:", decoded)
