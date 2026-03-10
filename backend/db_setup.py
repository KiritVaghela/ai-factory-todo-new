import sqlite3
import os

DB_NAME = 'tasks.db'

# Define the schema for the tasks table
TASKS_TABLE_SCHEMA = '''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
);
'''

def get_db_path():
    """
    Returns the absolute path to the database file.
    """
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), DB_NAME)

def initialize_database():
    """
    Initializes the SQLite database and creates the tasks table if it doesn't exist.
    """
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(TASKS_TABLE_SCHEMA)
    conn.commit()
    conn.close()
    print(f"Database initialized at {db_path}")

if __name__ == "__main__":
    initialize_database()
