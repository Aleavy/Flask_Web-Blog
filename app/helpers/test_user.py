from app.models.user import  Blog_User
from app.helpers.hash_password import hash_password
from dotenv import load_dotenv
import os
from app import db

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


def create_user():
    user_exist = Blog_User.query.get(1)
    if not user_exist:
        user1 = Blog_User(email=ADMIN_EMAIL, password= hash_password(ADMIN_PASSWORD), username='Admin')
        db.session.add(user1)
        db.session.commit()