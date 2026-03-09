import jwt
import datetime

SECRET_KEY = 'your_secret_key_here'  # Change this to a strong secret key

def create_token(data: dict, expires_in: int = 3600) -> str:
    expiration = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
    data['exp'] = expiration.timestamp()
    token = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return token


def decode_token(token: str) -> dict:
    try:
        decoded_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_data
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')