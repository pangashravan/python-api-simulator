# In-memory data store (simulates a database)

users_db = [
    {"id": 1, "name": "Shravan Yadav", "email": "shravan@example.com", "role": "admin"},
    {"id": 2, "name": "Alice Johnson", "email": "alice@example.com", "role": "user"},
    {"id": 3, "name": "Bob Smith", "email": "bob@example.com", "role": "user"},
]

products_db = [
    {"id": 1, "name": "Python Handbook", "price": 499.0, "category": "books", "stock": 50},
    {"id": 2, "name": "Mechanical Keyboard", "price": 3999.0, "category": "electronics", "stock": 20},
    {"id": 3, "name": "Coffee Mug", "price": 299.0, "category": "accessories", "stock": 100},
]

# Fast lookup indexes (kept in sync with lists)
users_index = {u['id']: u for u in users_db}
products_index = {p['id']: p for p in products_db}

def add_user(user: dict) -> None:
    users_db.append(user)
    users_index[user['id']] = user

def delete_user_by_id(user_id: int) -> None:
    global users_db
    users_db = [u for u in users_db if u['id'] != user_id]
    users_index.pop(user_id, None)

def add_product(product: dict) -> None:
    products_db.append(product)
    products_index[product['id']] = product

def delete_product_by_id(product_id: int) -> None:
    global products_db
    products_db = [p for p in products_db if p['id'] != product_id]
    products_index.pop(product_id, None)
