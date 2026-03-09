# ToDo App

## Setting Up

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ai-factory-todo-new
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   npm install
   ```

3. **Set up the database**:
   To set up the SQLite database, ensure you have SQLite installed and follow these commands:
   ```bash
   cd backend
   python db_setup.py
   ```

4. **Run the application**:
   - For the backend:
     ```bash
     uvicorn main:app --reload
     ```
   - For the frontend:
     ```bash
     npm run dev
     ```

5. **Access the application**:
   Navigate to `http://localhost:3000` in your web browser to access the application.

## Features
- Add, update, and delete tasks.
- Mark tasks as complete or incomplete.

## Development
- To contribute to the project, please follow the standard git workflow: create a branch, make your changes, and submit a pull request. 

## License
This project is licensed under the MIT License.