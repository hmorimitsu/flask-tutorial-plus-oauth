from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField, TextAreaField
from wtforms.validators import DataRequired, Length


class CreateForm(FlaskForm):
    title = TextField(
        'Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired(), Length(1, 500)])
    register = SubmitField('Register')


class UpdateForm(FlaskForm):
    title = TextField(
        'Title', validators=[DataRequired(), Length(1, 50)])
    body = TextAreaField('Body', validators=[DataRequired(), Length(1, 500)])
    save = SubmitField('Save')
    delete = SubmitField('Delete')
