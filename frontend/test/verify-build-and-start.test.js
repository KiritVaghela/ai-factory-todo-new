// This test verifies that the frontend build and start scripts work without errors.
// It runs `npm run build` and `npm start` (or `npm run dev` for Vite) and checks for errors.

const { execSync, spawn } = require('child_process');
const path = require('path');

const FRONTEND_DIR = path.resolve(__dirname, '..');

function runCommand(command, options = {}) {
  try {
    execSync(command, { stdio: 'inherit', ...options });
    return true;
  } catch (err) {
    return false;
  }
}

describe('Frontend build and start scripts', () => {
  jest.setTimeout(60000); // Allow up to 60 seconds for build/start

  test('npm run build completes without errors', () => {
    const result = runCommand('npm run build', { cwd: FRONTEND_DIR });
    expect(result).toBe(true);
  });

  test('npm run dev (start) launches without errors and responds', done => {
    // Start the dev server
    const devProcess = spawn('npm', ['run', 'dev'], {
      cwd: FRONTEND_DIR,
      env: { ...process.env, BROWSER: 'none' },
      stdio: ['ignore', 'pipe', 'pipe']
    });

    let output = '';
    let errorOutput = '';
    let started = false;

    devProcess.stdout.on('data', data => {
      output += data.toString();
      // Vite typically prints 'Local:' or 'ready in' when ready
      if (/Local:|ready in|VITE v/i.test(output) && !started) {
        started = true;
        devProcess.kill();
        done();
      }
    });
    devProcess.stderr.on('data', data => {
      errorOutput += data.toString();
    });
    devProcess.on('exit', code => {
      if (!started) {
        done(new Error('Dev server did not start successfully.\n' + errorOutput));
      }
    });
    // Timeout in case server doesn't start
    setTimeout(() => {
      if (!started) {
        devProcess.kill();
        done(new Error('Dev server did not start within timeout.\n' + errorOutput));
      }
    }, 20000);
  });
});
