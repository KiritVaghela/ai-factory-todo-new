# Frontend - React + Vite + Tailwind CSS

This is the frontend for the ToDo App, built with React, Vite, and Tailwind CSS.

## Requirements

- Node.js 18+
- npm (comes with Node.js)

## Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```
   - The app will be available at [http://localhost:3000](http://localhost:3000)

3. **Build for production:**
   ```bash
   npm run build
   ```
   - Output will be in the `dist/` directory.

## Linting

- Run linter:
  ```bash
  npm run lint
  ```

## Testing

- Run tests:
  ```bash
  npm test
  ```

## Configuration

- Vite config: `vite.config.js`
- Tailwind config: `tailwind.config.js`
- Babel config: `babel.config.js`

## Notes

- The frontend expects the backend API to be running at `http://localhost:8000` by default. Adjust API URLs in the code if you change backend ports or host.
- For CORS to work, ensure the backend allows requests from the frontend origin (see backend CORS settings).

## Running with Docker Compose

- The frontend is included in the root `docker-compose.yml` for easy orchestration with the backend.

---

## Troubleshooting

- If you change dependencies, rebuild Docker images: `docker-compose build --no-cache`
- If ports are in use, stop other services or change the port in `vite.config.js` and `docker-compose.yml`.
