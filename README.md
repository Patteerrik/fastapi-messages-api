# FastAPI Messages API

![CI](https://github.com/Patteerrik/fastapi-messages-api/actions/workflows/ci.yml/badge.svg)

Production-ready backend API built with **FastAPI**, **PostgreSQL**, and **Docker**.  
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

## Quick demo

Start the application:

```bash
docker compose up --build
```

# Create a message (unauthenticated endpoint):

```bash
curl -X POST http://localhost:8000/messages \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world"}'
```

# Call a protected endpoint (API key required):
```bash
curl http://localhost:8000/protected \
  -H "X-API-Key: dev-secret"
```

---

## Run locally
```bash
docker compose up --build
```
- API: http://localhost:8000
- Docs: http://localhost:8000/docs

---

## Run tests 
```bash
docker compose exec api pytest
````

---

## CI

GitHub Actions automatically builds containers and runs the full test
suite on every push and pull request.

---

## Local development vs CI

- Local development uses Docker Compose with PostgreSQL
- CI runs tests in an isolated container environment
- Environment variables are managed via .env locally and GitHub Secrets in CI

---

## Why this project

Built to demonstrate how a simple FastAPI service can be evolved into a
maintainable, production-ready backend using industry-standard tools
(PostgreSQL, Alembic, Docker, CI) while keeping a stable API contract.
