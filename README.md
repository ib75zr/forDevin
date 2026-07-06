# forDevin

A small Flask REST API exposing a single endpoint.

## Endpoint

`GET /users/<id>` — returns a user's `name` and `email` from an in-memory dictionary.

- Existing user → `200` with `{"name": ..., "email": ...}`
- Unknown id → `404` with `{"error": "User with id <id> not found"}`

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Test

```bash
pytest
```
