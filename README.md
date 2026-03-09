# ToDo App

## Introduction
This is a simple ToDo application built with FastAPI for the backend and React for the frontend. The application allows users to create, read, update, and delete tasks.

## Design Decisions
- **FastAPI** was chosen for the backend due to its high performance and automatic generation of API documentation.
- **SQLite** is used as the database for simplicity and ease of setup.
- **React** was selected for the frontend to build a dynamic user interface.

## Components Usage
### Backend
- `main.py`: The entry point of the application. Sets up FastAPI, adds middleware, and defines the root endpoint.
- `routers/tasks.py`: Contains the routes related to task operations including creating, retrieving, updating, and deleting tasks.
- `db_setup.py`: Manages the setup of the SQLite database.

### Frontend
- `src/App.jsx`: The main React component that handles task fetching and rendering.
- `src/TaskList.jsx`: A component for displaying the list of tasks.
- `src/DeleteButton.jsx`: A component for rendering a button to delete a task.

## Installation
1. Clone the repository.
2. Navigate to the backend and install dependencies with:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the frontend and install dependencies with:
   ```bash
   npm install
   ```
4. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```
5. Start the frontend development server:
   ```bash
   npm run dev
   ```

## Running Tests
To run tests for the backend, use:
```bash
pytest
```

## Contributing
Contributions are welcome! Please create an issue or submit a pull request for any proposed changes.

## License
This project is licensed under the MIT License.