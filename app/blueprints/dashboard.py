from flask import Blueprint, render_template, redirect, url_for, abort, current_app
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
import os
from PIL import Image
from app.models.posts import Blog_Post
from werkzeug.utils import secure_filename
from ..forms.delete import DeleteForm
from app import db
from ..forms.create_post import CreatePostForm
from ..forms.edit_post import EditPostForm
from datetime import datetime, timezone

bp = Blueprint("dashboard", __name__, template_folder="templates")

@bp.route("/")
@login_required
def dashboard():
    return render_template("user/dashboard.html")


@bp.route("/view_all_posts/<int:id>")
def view_all_posts(id):
    form = DeleteForm()
    posts = Blog_Post.query.filter_by(user_id=id).all()
    return render_template("user/view_all_posts.html", posts=posts, form=form)

@bp.route("/create_post", methods=["POST", "GET"])
@login_required
def create_post():
    form = CreatePostForm()
    user_id_folder = 'user-' + current_user.get_id()
    user_folder = os.path.join(
        current_app.static_folder, 'images', user_id_folder, 'post'
        ).replace('\\', '/')


    if form.validate_on_submit():
        f = form.file.data

        filename = secure_filename(f.filename)
        image = Image.open(f.stream)
        image = image.convert("RGB")
        webp_filename = os.path.splitext(filename)[0] + ".webp"
        webp_path = os.path.join(user_folder, webp_filename)
        image.save(webp_path, format="webp", optimize=True, quality=80)
        if filename:
                #check that the 'images/post/<user>' folder exists, else it creates it 
            if not os.path.exists(user_folder):
                    os.makedirs(os.path.join(
                        user_folder
                        ))
            images = os.listdir(os.path.join(
                            user_folder
                            ))
            if webp_filename in images:
                num = 0
                filename_copy = webp_filename
                while filename_copy in images:
                    filename_copy = ""
                    num += 1
                    list_filename = filename.split(".")
                    only_name = list_filename[0]
                    only_name += f"({num})."
                    list_filename[0] = only_name
                    filename_copy = "".join(list_filename)
                
                filename = secure_filename(filename_copy)
            try:

                #built-in flask-wtf function to save images

                #charging post to database, only storing path to the image in the database
                post = Blog_Post(
                    title= form.title.data, 
                    body=form.body.data, 
                    image = webp_filename,
                    user_id = current_user.id,
                    author= current_user.username,
                    date_created=datetime.now(timezone.utc)
                    )
                db.session.add(post)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                    current_app.log_exception(f'There was an error uploading the image: {e=}')
                    abort(400)
            except Exception as e:
                return f"There was an error with creating the post: {e=}"
    return render_template("posts/create_post.html", form=form)

@bp.route('edit_post/<int:id>', methods=["GET", "POST"])
@login_required
def edit_post(id):
    user_id_folder = 'user-' + current_user.get_id()
    user_folder = os.path.join(
        current_app.static_folder, 'images', user_id_folder, 'post'
        ).replace('\\', '/')
    post = Blog_Post.query.filter_by(id=id).first()
    form = EditPostForm(obj=post)

    if current_user.username != post.author:
        abort(404)
        return
    if form.validate_on_submit():
        try:
            f = form.file.data
            filename = secure_filename(f.filename)
            
            if filename:
                images = os.listdir(os.path.join(
                                user_folder
                                ))
                if filename in images:
                    num = 0
                    filename_copy = filename
                    while filename_copy in images:
                        filename_copy = ""
                        num += 1
                        list_filename = filename.split(".")
                        only_name = list_filename[0]
                        only_name += f"({num})."
                        list_filename[0] = only_name
                        filename_copy = "".join(list_filename)
                    
                    filename = secure_filename(filename_copy)
                try:
            #check that the 'images/post/<user>' folder exists, else it creates it 
                    if not os.path.exists(user_folder):
                            os.makedirs(os.path.join(
                                user_folder
                                ))
                    #built-in flask-wtf function to save images
                    final_save = os.path.join(
                        user_folder, filename
                    ).replace('\\', '/')
                    f.save(final_save)
                except Exception as e:
                    return f"There was a problem saving the image while editing the post, {e=}"

                post.title = form.title.data
                post.body = form.body.data
                post.image = filename
                post.edited = datetime.now(timezone.utc)
                db.session.commit()
                return redirect(url_for('home.blog_post', id=post))
        except Exception as e:
            return f"There was an error editing the post. {e=}"
    return render_template('posts/edit_post.html', post=post, form=form)


@bp.route("/delete/<int:id>", methods=["POST", "GET"])
def delete(id):
    error = ""
    try:
        post = Blog_Post.query.filter_by(id=id).first()
        post_name = post.image
        form = DeleteForm()
        if form.validate_on_submit():
            try:
                if post_name != "test_image.png":
                    user_id_folder = 'user-' + current_user.get_id()
                    user_folder = os.path.join(
                    current_app.static_folder, 'images', user_id_folder, 'post', post_name
                    ).replace('\\', '/')
                    os.remove(user_folder)
                    print(f"Delete of {post_name} was ok")
            except Exception as e:
                 return f"There was an error deleting the image; {e=}"
            db.session.delete(post)
            db.session.commit()
            return redirect(url_for("dashboard.view_all_posts", id=current_user.id))
    except Exception as e:
        error = f"There was a problem deleting the post: {e}"

    return error
