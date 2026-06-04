def validate_request(method):
    allowed_methods = ["GET", "POST"]

    return method in allowed_methods

