# ToDo App
A simple and efficient ToDo application to manage daily tasks.

## Setup Instructions
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.

## Run Instructions
Run the application using `uvicorn main:app --reload`.

## API Endpoint Examples
- Register User: `POST /users/register`
- Login User: `POST /users/login`
- Create Task: `POST /tasks/`
- Get Tasks: `GET /tasks/`
- Delete Task: `DELETE /tasks/{task_id}`