from flask import Blueprint, flash, redirect, render_template, current_app
from flask_login import login_user, login_required, logout_user, login_manager
from werkzeug.security import check_password_hash
from app.helpers.hash_password import hash_password
from app.models.user import Blog_User
from app.forms.sign_up import SignUpForm
from app.forms.login import LoginForm

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    db = current_app.extensions["sqlalchemy"]
    form = SignUpForm()
    if form.validate_on_submit():
        try:
            # check if user have an account
            check = db.session.execute(db.select(Blog_User).filter_by(email=form.email.data)).scalar()
            if check:
                flash("You already have an account!")
                return redirect(url_for("auth.sign_up"))
            # validates that the passwords are the same
            if form.password.data == form.confirm_password.data:
                username_exist = Blog_User.query.filter_by(username = form.username.data).first()
                if username_exist:
                    flash("The username is already taken")
                    return redirect(url_for("auth.sign_up"))
                try:
                    # inserting user in the database with password being hashed
                    user = Blog_User(email=form.email.data, password= hash_password(form.password.data), username=form.username.data)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for("auth.login"))
                except Exception as e:
                    return f"There was an error: {e}"
            else:
                flash("The passwords aren't the same, try again")
                return redirect(url_for("auth.sign_up"))
        except Exception as e:
            return f"There was an error with the signup. Error: {e}"
    return render_template("user/sign_up.html", form=form)


from flask import redirect, url_for



@auth.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    # Before i was using form.populate_obj() but then the login behaves weird
    # when i was tryng to access current user what i was getting was None, so
    # i just dump it and did it manually. 
    password = form.password.data
    email = form.email.data
    if form.validate_on_submit():
        # checking if the user have an account
        user = Blog_User.query.filter_by(email = email).first()
        try:
            if user:
                # comparing password if when reverting the hash of the password
                # they are equal
                if check_password_hash(password=password,pwhash=user.password):
                    login_user(user)

                    return redirect("/")
                else:
                    flash("The password or email was incorrect.")
                    return redirect("login")
            else:
                flash("You dont have an account.")
                return redirect("login")
        except Exception as e:
            return f"There was an error with the login: {e}"
    return render_template("user/login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    # logut function for flask-login
    try:
        logout_user()
        return redirect("/")
    except Exception as e:
        return f"There was an error with the logout. Error: {e}"