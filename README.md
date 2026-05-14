# Python REST API Simulator

A CLI-based API simulation engine built using Python to mimic backend request-response workflows.

---

## Features

- Simulates GET and POST requests
- JSON serialization and parsing
- Dynamic response generation
- Structured validation and exception handling
- Modular backend architecture

---

## Tech Stack

- Python
- JSON
- CLI
- Modular Programming

---

## Project Structure

```text
app/
├── main.py
├── routes.py
├── handlers.py
└── utils.py
```

---

## Example Request

```json
{
  "method": "GET",
  "endpoint": "/users"
}
```

---

## Example Response

```json
{
  "status": 200,
  "data": ["user1", "user2"]
}
```

---

## Learning Outcomes

- Backend request-response lifecycle
- API architecture basics
- Error handling patterns
- Code modularization

---

## Future Improvements

- FastAPI version
- Database integration
- Authentication layer
- Docker containerization
