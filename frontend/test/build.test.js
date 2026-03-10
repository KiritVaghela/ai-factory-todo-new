// build.test.js
// This test verifies that the Vite build process completes without errors.

const { execSync } = require('child_process');
const path = require('path');

describe('Vite Frontend Build', () => {
  it('should complete without errors', () => {
    // Run the build command in the frontend directory
    const frontendDir = path.resolve(__dirname, '..');
    let output = '';
    let error = '';
    try {
      output = execSync('npm run build', {
        cwd: frontendDir,
        stdio: 'pipe',
        encoding: 'utf-8',
        env: { ...process.env, CI: 'true' },
      });
    } catch (err) {
      error = err.stdout || err.stderr || err.message;
    }
    if (error) {
      // Print the error output for debugging
      console.error('Build failed:', error);
    }
    expect(error).toBeFalsy();
    expect(output).toMatch(/dist/);
    expect(output).toMatch(/built in|Build completed|build/i);
  });
});
