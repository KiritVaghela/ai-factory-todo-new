# models.py
# User model and authentication logic for demo purposes
import sqlite3
from typing import Optional, Dict
import hashlib

DATABASE = "backend/tasks.db"

# --- User Model ---

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_user_table():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def hash_password(password: str) -> str:
    # Simple SHA256 hash for demo (not for production)
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def create_demo_user():
    """
    Create a hardcoded demo user if not exists.
    Username: demo
    Password: demo123
    """
    username = "demo"
    password = "demo123"
    password_hash = hash_password(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )
    user = cursor.fetchone()
    if not user:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
    conn.close()


def authenticate_user(username: str, password: str) -> Optional[Dict]:
    """
    Authenticate user by username and password.
    Returns user dict if authenticated, else None.
    """
    password_hash = hash_password(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password_hash = ?",
        (username, password_hash)
    )
    user = cursor.fetchone()
    conn.close()
    if user:
        return dict(user)
    return None

# --- Initialization ---

# Ensure user table and demo user exist on import
create_user_table()
create_demo_user()
