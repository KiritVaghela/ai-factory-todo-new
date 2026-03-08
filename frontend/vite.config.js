import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    cors: {
      origin: '*', // Allow all origins for development
      methods: ['GET', 'POST', 'PUT', 'DELETE'], // Allowed methods
      allowedHeaders: ['Content-Type', 'Authorization'], // Allowed headers
    },
  },
});