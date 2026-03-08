# Todo App
A simple and efficient Todo application to manage personal or professional tasks.

## Setup Instructions
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.

## Run Instructions
Run the application using:
```bash
uvicorn main:app --reload
```

## API Endpoint Examples
- `GET /todos` - Fetch all todo items
- `POST /todos` - Create a new todo item
- `PUT /todos/{id}` - Update an existing todo item
- `DELETE /todos/{id}` - Delete a todo item