# AI Factory ToDo Application

This project is a full-stack ToDo application with a FastAPI backend and a React frontend.

## Project Structure

- `backend/`: Contains the FastAPI backend code.
- `frontend/`: Contains the React frontend code.

## Running the Application

### Backend

1. Navigate to the `backend` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Initialize the database:
   ```bash
   python db_setup.py
   ```
4. Run the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Run the frontend development server:
   ```bash
   npm run dev
   ```

## Code Validation

You can validate the code quality and style using the following commands:

### Using `init` command

Run the following command in the `backend` directory to initialize and validate the code:

```bash
./lint.sh init
```

This will set up the necessary environment and run validation checks.

### Using `lint` command

To run linting and code validation checks, use:

```bash
./lint.sh lint
```

This will check the code for style issues and potential errors.

Make sure you have the necessary linters and tools installed as specified in the `backend/requirements.txt` or `lint.sh` script.

## Additional Information

- The backend API is accessible at `http://localhost:8000` by default.
- The frontend runs on `http://localhost:3000`.

## License

This project is licensed under the MIT License.
