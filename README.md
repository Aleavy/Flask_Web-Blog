# Features
- Auth.
- CRUD operations.
- Full responsivenes.
- Security.
- Form security enchanced.
- Create, delete and update post.

# Screens

## Home
- Here u see all the posts in a grid like view.
![alt text](https://github.com/Aleavy/Flask_Web-Blog/blob/main/app/static/img/home.jpg?raw=true)

## Dashboard
- U can view all the post u have.
- Delete posts.
- Go to the post selected.
- Edit the post.
![alt text](https://github.com/Aleavy/Flask_Web-Blog/blob/main/app/static/img/viewallpost.jpg?raw=true)

- Create a post.
![alt text](https://github.com/Aleavy/Flask_Web-Blog/blob/main/app/static/img/createpost.jpg?raw=true)

## Create Post
- When creating your post, u are seing how will be to your end reader, asuring expected final results.
![alt text](https://github.com/Aleavy/Flask_Web-Blog/blob/main/app/static/img/createpost.jpg?raw=true)

## Post
- View of the post
![alt text](https://github.com/Aleavy/Flask_Web-Blog/blob/main/app/static/img/post.jpg?raw=true)

## Auth
- Login
![alt text](https://github.com/Aleavy/Flask_Web-Blog/blob/main/app/static/img/login.jpg?raw=true)

- Sign Up
![alt text](https://github.com/Aleavy/Flask_Web-Blog/blob/main/app/static/img/signup.jpg?raw=true)

# Instalation guide

## Copy the repository:
```
git clone https://github.com/Aleavy/Flask_Web-Blog.git
```

## Go to the folder where the repo was clone and install the requirementents:
```
pip install -r requirements.txt
```

## Create two secret keys and saved them for later:
```
python -c 'import secrets; print(secrets.token_hex())'
```

## make a .env file in the root level in the directory with:

```
SECRET_KEY = "First Secret KEY here"
STRIPE_API_KEY = 'Second Secret KEY here'
SQLALCHEMY_DATABASE_URI = "sqlite:///name_of_your_database.db"
ADMIN_EMAIL = "admin mail"
ADMIN_PASSWORD = "password here

#Optional If u want the page with preloaded posts for testing or for seing the aesthetic, if not just dont define it.
CREATE_TEST_POSTS = "TRUE"
```

## Then finally, run the project:
```
python run.py
```

# License
This project is under MIT license, more info in LICENSE.txt
