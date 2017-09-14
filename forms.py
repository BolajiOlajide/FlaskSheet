from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class AddTodoForm(FlaskForm):
    name = StringField('task', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    status = BooleanField()
