import sqlite3

DATABASE = 'todos.db'

def create_connection():
    conn = sqlite3.connect(DATABASE)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        completed BOOLEAN NOT NULL DEFAULT 0
                    )''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()