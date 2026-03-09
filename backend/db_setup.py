import sqlite3

DATABASE = 'tasks.db'

# Initialize the databases with required tables
def init_tasks_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
                          id INTEGER PRIMARY KEY,
                          title TEXT NOT NULL,
                          completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
                      );''')
    conn.close()

if __name__ == '__main__':
    init_tasks_db()
