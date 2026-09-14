# Contributing to Real-Time E-Commerce Insights Engine

Thank you for your interest in contributing to the **Real-Time E-Commerce Insights Engine**! 🎉 We welcome contributions of all kinds: bug fixes, new features, analytics optimizations, documentation improvements, and feedback.

Please take a few moments to review this guide before getting started.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Submitting Pull Requests](#submitting-pull-requests)
- [Local Development Setup](#local-development-setup)
  - [Prerequisites](#prerequisites)
  - [Step-by-Step Setup](#step-by-step-setup)
  - [Running with Docker](#running-with-docker)
- [Coding Standards & Linting](#coding-standards--linting)
- [Commit & Pull Request Guidelines](#commit--pull-request-guidelines)
  - [Branch Naming](#branch-naming)
  - [Commit Messages](#commit-messages)
  - [Pull Request Checklist](#pull-request-checklist)

---

## Code of Conduct

We are committed to providing a friendly, safe, and welcoming environment for all contributors. Please be respectful, constructive, and considerate in all communications, issues, and pull requests.

---

## How Can I Contribute?

### Reporting Bugs

Before reporting a bug, please check existing issues to ensure it hasn't already been reported.

When creating a bug report, please include:
- A clear, descriptive title.
- Steps to reproduce the behavior.
- Expected vs. actual behavior.
- Error logs / stack traces.
- Your environment details (OS, Python version, Docker version).

> [!IMPORTANT]
> If you discover a security vulnerability, please refer to our [SECURITY.md](SECURITY.md) and report it privately instead of opening a public issue.

### Suggesting Features

We welcome ideas for new analytical metrics, API endpoints, performance optimizations, or Docker improvements!
- Open an issue describing the proposed feature and why it would be beneficial.
- Outline potential implementation details or API contract designs if applicable.

---

## Local Development Setup

### Prerequisites

- **Python 3.12+**
- **Git**
- **Docker & Docker Compose** *(optional, for containerized development)*

### Step-by-Step Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/ecommerce-insights-api.git
   cd ecommerce-insights-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On macOS/Linux:
   python3 -m venv .venv
   source .venv/bin/activate

   # On Windows:
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install ruff pytest
   ```

4. **Generate the mock dataset:**
   ```bash
   cd app
   python generate_data.py
   cd ..
   ```

5. **Start the development server:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser to explore the interactive Swagger documentation.

### Running with Docker

You can also run the full application in a containerized environment:

```bash
docker compose up --build
```

---

## Coding Standards & Linting

We maintain high code quality and consistency across the repository:

- **Type Hints:** Use standard Python type annotations wherever feasible.
- **DataFrames:** Prefer vectorized Pandas operations over iterative loops.
- **Linting & Formatting:** We use **Ruff** for linting and formatting. Ensure your code passes all checks before opening a pull request:

```bash
# Check for lint errors
ruff check .

# Automatically fix fixable lint issues
ruff check --fix .

# Check code formatting
ruff format --check .

# Format code
ruff format .
```

Configuration details can be reviewed in [ruff.toml](ruff.toml).

---

## Commit & Pull Request Guidelines

### Branch Naming

Create a dedicated branch for your work using a descriptive prefix:

- `feature/summary-metrics-export`
- `fix/missing-timezone-dtz`
- `docs/update-contributing-guide`
- `refactor/services-load-data`

### Commit Messages

We encourage following the [Conventional Commits](https://www.conventionalcommits.org/) specification:

- `feat: add hourly sales breakdown endpoint`
- `fix: resolve FileNotFoundError when mounting Docker volumes`
- `docs: update setup instructions in README`
- `refactor: optimize category aggregation in services.py`
- `test: add unit tests for summary calculations`

### Pull Request Checklist

Before submitting your PR, please verify:

- [ ] Your code passes all linter checks (`ruff check .`).
- [ ] Any new dependencies are documented and added to `requirements.txt` if necessary.
- [ ] Documentation ([README.md](README.md), docstrings, API docs) is updated if your changes introduce new endpoints or change behaviors.
- [ ] Your PR description clearly explains what problem it solves and references any related issue numbers (e.g., `Closes #12`).

Thank you for contributing to the **Real-Time E-Commerce Insights Engine**! 🚀
