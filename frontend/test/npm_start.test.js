const { exec } = require('child_process');
const fs = require('fs');

describe('NPM Start Command', () => {
  it('should start the app without errors', (done) => {
    exec('npm run start', (error, stdout, stderr) => {
      console.log(stdout);
      console.error(stderr);
      // Assertions
      expect(error).toBeNull();
      expect(stdout).toContain('Vite');  // Expect output to indicate Vite is running
      done();
    });
  });
});
