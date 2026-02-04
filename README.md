# FastAPI Messages API

Production-ready backend API built with FastAPI, PostgreSQL, and Docker.
Demonstrates clean architecture, database migrations, automated testing,
and continuous integration.

---

## Tech Stack

- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Docker & Docker Compose
- Pytest
- GitHub Actions

---

## Architecture

```text
app/
├─ main.py
├─ core/
│  ├─ config.py
│  └─ security.py
├─ routers/
│  └─ messages.py
├─ database.py
├─ deps.py
├─ models.py
alembic/
tests/
```

---

## Features 

- API key protected endpoints
- Persistent PostgreSQL storage
- Database migrations with Alembic
- Dependency-injected DB sessions
- Automated tests with pytest
- CI pipeline running tests on push

---

## Run locally

- docker compose up --build
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

---

## Run tests 

- docker compose exec api pytest

---

## CI

GitHub Actions runs the test suite on every push.

---

## Why this project

Built to demonstrate how a simple FastAPI service can be evolved into a
maintainable, production-ready backend using industry-standard tools
(PostgreSQL, Alembic, Docker, CI) while keeping a stable API contract.

---

## Local development vs CI

- Local development uses Docker Compose with PostgreSQL
- CI runs tests in an isolated container environment
- Environment variables are managed via .env locally and GitHub Secrets in CI
