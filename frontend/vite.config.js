import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    open: true,
    strictPort: true,
    watch: {
      usePolling: true,
      interval: 1000
    }
  },
  build: {
    outDir: 'dist',
    rollupOptions: {
      output: {
        format: 'esm'
      }
    }
  },
  esbuild: {
    drop: ['console', 'debugger'],
    jsxFactory: 'React.createElement',
    jsxFragment: 'React.Fragment'
  }
});