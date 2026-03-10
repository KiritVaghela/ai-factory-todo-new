# backend/models.py
from typing import Optional, Dict, List
from pydantic import BaseModel
import hashlib

# --- User Model ---
class User(BaseModel):
    username: str
    password_hash: str  # Store hashed password
    full_name: Optional[str] = None
    email: Optional[str] = None

# --- In-memory User Store (stub) ---
class UserStore:
    def __init__(self):
        # username -> User
        self._users: Dict[str, User] = {}
        # Add a default user for testing
        self.create_user("admin", "admin123", full_name="Administrator", email="admin@example.com")

    def hash_password(self, password: str) -> str:
        # Simple hash for demonstration (do NOT use in production)
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    def create_user(self, username: str, password: str, full_name: Optional[str] = None, email: Optional[str] = None) -> User:
        if username in self._users:
            raise ValueError("User already exists")
        password_hash = self.hash_password(password)
        user = User(username=username, password_hash=password_hash, full_name=full_name, email=email)
        self._users[username] = user
        return user

    def authenticate(self, username: str, password: str) -> Optional[User]:
        user = self._users.get(username)
        if not user:
            return None
        if user.password_hash == self.hash_password(password):
            return user
        return None

    def get_user(self, username: str) -> Optional[User]:
        return self._users.get(username)

    def list_users(self) -> List[User]:
        return list(self._users.values())

# Singleton instance for use in routers, etc.
user_store = UserStore()
