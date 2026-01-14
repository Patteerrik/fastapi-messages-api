# FastAPI Messages API

A small, focused backend API built with **FastAPI** and **SQLAlchemy**.
The project demonstrates clean API design, separation of concerns, and
persistent storage using SQLite.

The API was built incrementally to show how the implementation can evolve
(from in-memory storage to a real database) **without changing the API contract**.

---

## Features

- REST API with FastAPI
- Clear separation of concerns:
  - Pydantic schemas (API contracts)
  - SQLAlchemy models (database layer)
  - Feature-based routers
- SQLite persistence
- Request & response validation
- Interactive Swagger documentation

---

## API Endpoints

### Create a message
**POST `/messages`**

Request:
```json
{ "text": "Hello world" }
