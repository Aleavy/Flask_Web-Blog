from flask import Blueprint, flash, redirect, render_template, current_app, send_from_directory
from flask_login import login_required
from ..models.posts import Blog_Post


home_page = Blueprint("home", __name__, template_folder="templates")



@home_page.route("/", methods=['GET'])
def start():
    db = current_app.extensions["sqlalchemy"]
    posts = db.session.execute(db.select(Blog_Post).order_by(Blog_Post.date_created.desc())).scalars()
    return render_template("index.html", posts = posts)

# It was a function to show files in a folder. 
@home_page.route('/static/user-<user>/post/<filename>')
def show_images(user, filename):
    # print(f"{user=}")
    user_folder = f"{current_app.static_folder}/images/user-{user}/post"
    return send_from_directory(user_folder, filename)





@home_page.route("/post/<id_slug:id>")
def blog_post(id):
    db = current_app.extensions["sqlalchemy"]
    post = Blog_Post.query.filter_by(id=id).first()
    print(post.edited)
    return render_template("posts/post-view.html", post=post)