# Frontend

This directory contains the frontend React application for the ToDo app.

## Available Scripts

In the project directory, you can run:

### `npm install`

Installs the dependencies.

### `npm run dev`

Runs the app in development mode.

### `npm run build`

Builds the app for production.

### `npm run preview`

Previews the production build locally.

### `npm run lint`

Runs the linter to check for code style and errors.

### `npm run lint:fix`

Runs the linter and automatically fixes problems.

### `./lint-frontend.sh`

Runs the frontend lint script.

## Linting

To check the code for linting errors, run:

```bash
npm run lint
```

Or you can run the provided lint script directly:

```bash
./lint-frontend.sh
```

This will run ESLint on the frontend source files and report any issues.

## Configuration

- ESLint configuration is in `.eslintrc.json`.
- Babel configuration is in `babel.config.js`.
- Tailwind CSS configuration is in `tailwind.config.js`.
- Vite configuration is in `vite.config.js`.

## Notes

Make sure to run linting before committing your code to maintain code quality.
