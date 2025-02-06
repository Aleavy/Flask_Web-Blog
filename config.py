from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

#Code to generate secret key: python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv("SECRET_KEY")
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
DEBUG = False
BCRYPT_LEVEL = 12 # Configuration for the Flask-Bcrypt extension