// lint-check.js
// Runs ESLint on all JS/JSX files in src/ and root of frontend, exits with error if any syntax errors are found.

const { ESLint } = require('eslint');
const path = require('path');

(async function main() {
  try {
    const eslint = new ESLint({
      extensions: ['.js', '.jsx'],
      errorOnUnmatchedPattern: false,
    });

    // Files to lint: all .js/.jsx in src/ and root
    const filesToLint = [
      path.join(__dirname, 'src', '**', '*.js'),
      path.join(__dirname, 'src', '**', '*.jsx'),
      path.join(__dirname, '*.js'),
      path.join(__dirname, '*.jsx'),
    ];

    const results = await eslint.lintFiles(filesToLint);
    const formatter = await eslint.loadFormatter('stylish');
    const resultText = formatter.format(results);

    // Check for syntax errors
    let hasSyntaxError = false;
    for (const result of results) {
      for (const message of result.messages) {
        if (message.fatal || message.severity === 2) {
          if (message.fatal || message.message.includes('Parsing error')) {
            hasSyntaxError = true;
          }
        }
      }
    }

    if (resultText) {
      console.log(resultText);
    }

    if (hasSyntaxError) {
      console.error('\u001b[31mSyntax errors detected by ESLint. Please fix them before committing.\u001b[0m');
      process.exit(1);
    } else {
      console.log('\u001b[32mNo syntax errors detected by ESLint.\u001b[0m');
    }
  } catch (err) {
    console.error(err);
    process.exit(2);
  }
})();
