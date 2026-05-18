"""
Python REST API Simulator
A Flask-based REST API demonstrating backend fundamentals:
- GET / POST / PUT / DELETE endpoints
- JSON request & response handling
- Input validation & error handling
- Modular structure
"""

from flask import Flask, jsonify, request
from validators import validate_user, validate_product
from db import users_db, products_db

app = Flask(__name__)


# ── Root ──────────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return jsonify({
        "message": "Python REST API Simulator",
        "version": "1.0",
        "endpoints": {
            "users": "/api/users",
            "products": "/api/products",
            "health": "/api/health"
        }
    })


# ── Health Check ──────────────────────────────────────────────────────────────
@app.route('/api/health')
def health():
    return jsonify({"status": "running", "message": "API is healthy"})


# ── USERS ─────────────────────────────────────────────────────────────────────
@app.route('/api/users', methods=['GET'])
def get_users():
    """Return all users"""
    return jsonify({"success": True, "count": len(users_db), "users": users_db})


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Return a single user by ID"""
    user = next((u for u in users_db if u['id'] == user_id), None)
    if not user:
        return jsonify({"success": False, "error": "User not found"}), 404
    return jsonify({"success": True, "user": user})


@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    error = validate_user(data)
    if error:
        return jsonify({"success": False, "error": error}), 400

    new_user = {
        "id": len(users_db) + 1,
        "name": data['name'].strip(),
        "email": data['email'].strip().lower(),
        "role": data.get('role', 'user')
    }
    users_db.append(new_user)
    return jsonify({"success": True, "message": "User created", "user": new_user}), 201


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    user = next((u for u in users_db if u['id'] == user_id), None)
    if not user:
        return jsonify({"success": False, "error": "User not found"}), 404

    data = request.get_json()
    if 'name' in data:
        user['name'] = data['name'].strip()
    if 'email' in data:
        user['email'] = data['email'].strip().lower()
    if 'role' in data:
        user['role'] = data['role']

    return jsonify({"success": True, "message": "User updated", "user": user})


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    global users_db
    user = next((u for u in users_db if u['id'] == user_id), None)
    if not user:
        return jsonify({"success": False, "error": "User not found"}), 404

    users_db = [u for u in users_db if u['id'] != user_id]
    return jsonify({"success": True, "message": f"User {user_id} deleted"})


# ── PRODUCTS ──────────────────────────────────────────────────────────────────
@app.route('/api/products', methods=['GET'])
def get_products():
    """Return all products, with optional category filter"""
    category = request.args.get('category')
    if category:
        filtered = [p for p in products_db if p['category'].lower() == category.lower()]
        return jsonify({"success": True, "count": len(filtered), "products": filtered})
    return jsonify({"success": True, "count": len(products_db), "products": products_db})


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Return a single product by ID"""
    product = next((p for p in products_db if p['id'] == product_id), None)
    if not product:
        return jsonify({"success": False, "error": "Product not found"}), 404
    return jsonify({"success": True, "product": product})


@app.route('/api/products', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.get_json()
    error = validate_product(data)
    if error:
        return jsonify({"success": False, "error": error}), 400

    new_product = {
        "id": len(products_db) + 1,
        "name": data['name'].strip(),
        "price": float(data['price']),
        "category": data.get('category', 'general'),
        "stock": int(data.get('stock', 0))
    }
    products_db.append(new_product)
    return jsonify({"success": True, "message": "Product created", "product": new_product}), 201


# ── Error Handlers ─────────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return jsonify({"success": False, "error": "Route not found"}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"success": False, "error": "Method not allowed"}), 405


@app.errorhandler(500)
def internal_error(e):
    return jsonify({"success": False, "error": "Internal server error"}), 500


if __name__ == '__main__':
    print("Starting Python REST API Simulator...")
    print("Visit: http://127.0.0.1:5000")
    app.run(debug=True)
