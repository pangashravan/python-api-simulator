# Input validation functions

def validate_user(data):
    """Validate user creation payload. Returns error string or None."""
    if not data:
        return "Request body is required"
    if not data.get('name') or not str(data['name']).strip():
        return "Field 'name' is required and cannot be empty"
    if not data.get('email') or not str(data['email']).strip():
        return "Field 'email' is required and cannot be empty"
    if '@' not in str(data['email']):
        return "Field 'email' must be a valid email address"
    return None


def validate_product(data):
    """Validate product creation payload. Returns error string or None."""
    if not data:
        return "Request body is required"
    if not data.get('name') or not str(data['name']).strip():
        return "Field 'name' is required and cannot be empty"
    if data.get('price') is None:
        return "Field 'price' is required"
    try:
        price = float(data['price'])
        if price < 0:
            return "Field 'price' must be a positive number"
    except (ValueError, TypeError):
        return "Field 'price' must be a valid number"
    return None
