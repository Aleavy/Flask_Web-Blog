from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired

class DeleteForm(FlaskForm):
    delete = SubmitField("Delete", validators=[DataRequired("There must be data?")])
