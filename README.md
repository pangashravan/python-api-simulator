# Python REST API Simulator

A Flask-based REST API demonstrating core backend engineering concepts — request handling, JSON serialisation, input validation, modular code structure, and proper HTTP status codes.

## Features

- Full CRUD endpoints for Users and Products
- JSON request/response handling
- Input validation with descriptive error messages
- Modular architecture (app, db, validators)
- HTTP status codes (200, 201, 400, 404, 405, 500)

## Tech Stack

- Python 3.x
- Flask
- REST API Design
- JSON / HTTP

## Setup & Run

```bash
# Clone the repo
git clone https://github.com/pangashravan/python-api-simulator.git
cd python-api-simulator

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

Server runs at: `http://127.0.0.1:5000`

## API Endpoints

### Users

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users` | Get all users |
| GET | `/api/users/<id>` | Get user by ID |
| POST | `/api/users` | Create new user |
| PUT | `/api/users/<id>` | Update user |
| DELETE | `/api/users/<id>` | Delete user |

### Products

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products` | Get all products |
| GET | `/api/products?category=books` | Filter by category |
| GET | `/api/products/<id>` | Get product by ID |
| POST | `/api/products` | Create new product |

### Other

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/api/health` | Health check |

## Example Requests

```bash
# Get all users
curl http://127.0.0.1:5000/api/users

# Create a user
curl -X POST http://127.0.0.1:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Shravan", "email": "shravan@example.com"}'

# Get products by category
curl http://127.0.0.1:5000/api/products?category=books
```

## Author

**Panga Shravan Yadav** — Python Developer | Backend Engineer  
[LinkedIn](https://www.linkedin.com/in/pangashravan) | [GitHub](https://github.com/pangashravan)
