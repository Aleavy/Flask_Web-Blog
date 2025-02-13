from flask import current_app
from werkzeug.security import generate_password_hash

def hash_password(password):
    return generate_password_hash(
        password,
        method="pbkdf2:sha256",
        salt_length=8
    )