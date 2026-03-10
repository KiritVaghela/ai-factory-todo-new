# Backend Linting Setup

This backend project uses Python and FastAPI. To ensure code quality and style compliance, we use `flake8` as the linter.

## Setup

1. Install flake8:

```bash
pip install flake8
```

2. Run linting:

```bash
flake8 .
```

This will check all Python files in the backend directory for style and quality issues.

## Optional: Add a lint script

You can add a script in your `backend/` directory or your project root to run linting easily.

Example:

```bash
#!/bin/bash
flake8 backend/
```

Make it executable:

```bash
chmod +x lint.sh
```

Then run:

```bash
./lint.sh
```

## Integrate with CI/CD

Add the lint command to your CI pipeline to enforce code quality on every commit.

---

# flake8 Configuration

You can add a `.flake8` config file in the `backend/` directory to customize linting rules.

Example `.flake8`:

```
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

Adjust rules as needed.
