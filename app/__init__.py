import os
from flask import Flask, redirect, flash, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .helpers.id_slug_converter import IDSlugConverter
from dotenv import load_dotenv




db = SQLAlchemy()
moment = Moment()
login_manager = LoginManager()

def create_app(config_class="config"):
    load_dotenv()

    """To create the app"""
    CREATE_TEST_POST = os.getenv("CREATE_TEST_POSTS")

    name_dir = os.path.abspath("instance")

    app = Flask(__name__, instance_path= name_dir)


    """To load configuration variables from an instance folder, we use app.config.from_pyfile(). If we set instance_relative_config=True when we create our app with the Flask() call, app.config.from_pyfile() will load the specified file from the instance/ directory."""

    #This is do it so we can access variables defined in config.py like a dictionary by app.config["variable_name"]
    app.config.from_object("config") 
    app.url_map.converters["id_slug"] = IDSlugConverter
    db.init_app(app)
    moment.init_app(app=app)
    login_manager.init_app(app)


    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        # This is neccesary for login to work, it just returns the row of the user logged
        from app.models.user import Blog_User
        user = Blog_User.query.get(user_id)
        # print(f"Loading user: {user} with user id: {user_id}")  # Debugging
        return user

    @login_manager.unauthorized_handler
    def handle_unauthorized():
        flash("You need to login to access there.")
        return redirect(url_for("auth.login"))

    from .blueprints.dashboard import bp
    from .blueprints.auth import auth
    from .blueprints.home import home_page
    app.register_blueprint(bp, url_prefix='/dashboard')
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(home_page, url_prefix="/")

    #to create the tables with test data
    with app.app_context():


        db.create_all()
        from app.helpers.test_post import create_post
        from app.helpers.test_user import create_user
        create_user()
        if CREATE_TEST_POST is not None:
            create_post()

    return app