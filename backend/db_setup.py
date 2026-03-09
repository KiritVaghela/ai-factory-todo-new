import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create tasks table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT 0
);
''')

# Function to insert initial data
def insert_initial_data():
    cursor.execute('''INSERT INTO tasks (title, completed) VALUES (?, ?)''', ('Sample Task 1', False))
    cursor.execute('''INSERT INTO tasks (title, completed) VALUES (?, ?)''', ('Sample Task 2', True))
    conn.commit()

# Uncomment the line below to insert initial data if needed
# insert_initial_data()

# Close the connection
conn.close()