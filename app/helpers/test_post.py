from app.models.posts import  Blog_Post
from app.helpers.test_data import POST_BODY, POST_TITLE, ADMIN_AUTHOR, ADMIN_FOLDER, TEST_IMAGE, SOURCE_IMAGE_PATH
from app import db
import shutil

import os


def create_post():
    post_exist = Blog_Post.query.first()
    if not post_exist:
        try:
            try:
                os.makedirs(ADMIN_FOLDER)
                if not os.path.exists(os.path.join(ADMIN_FOLDER, TEST_IMAGE)):
                    shutil.copy(os.path.join(SOURCE_IMAGE_PATH, TEST_IMAGE), ADMIN_FOLDER)
            except FileExistsError:
                print(f"{ADMIN_FOLDER} already exist.")
            print(f"{TEST_IMAGE} copied to {ADMIN_FOLDER}")
            post1 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                image= TEST_IMAGE,
                user_id = 1
                )
            post2 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                image= TEST_IMAGE,
                user_id = 1
                )
            post3 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                image= TEST_IMAGE,
                user_id = 1
                )
            post4 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                image= TEST_IMAGE,
                user_id = 1
                )
            post5 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                user_id = 1,
                image= TEST_IMAGE
                )
            post6 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                image= TEST_IMAGE,
                user_id = 1
                )
            post7 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                image= TEST_IMAGE,
                user_id = 1
                )
            post8 = Blog_Post(
                author= ADMIN_AUTHOR, 
                title=POST_TITLE, 
                body=POST_BODY, 
                image= TEST_IMAGE,
                user_id = 1
                )
            
            db.session.add(post1)
            db.session.add(post2)
            db.session.add(post3)
            db.session.add(post4)
            db.session.add(post5)
            db.session.add(post6)
            db.session.add(post7)
            db.session.add(post8)
            
            db.session.commit()
        except Exception as e:
            print(f"There was an error creating the admin post. {e=}")
