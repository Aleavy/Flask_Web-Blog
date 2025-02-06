from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length


class CreatePostForm(FlaskForm):
    title = TextAreaField("Title", validators=[DataRequired("This field cannot be empty"), Length(min=10, message="The text have to be at least 10 characters", max=100)])
    body = TextAreaField("Body", validators=[DataRequired("This cannot be empty"), Length(min=100)])
    file = FileField('File', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'svg'], "Only upload Images.")])
