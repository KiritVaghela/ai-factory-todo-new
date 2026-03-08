import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    cors: {
      origin: 'http://localhost:3000',  // Adjust this to your frontend's origin
      credentials: true
    }
  }
});