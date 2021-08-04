from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField,
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(FlaskForm):
    phonenumber = IntegerField('Password', validators=[DataRequired()])
    name = SubmitField('Confirm Password', validators = [DataRequired(), EqualTo("required")])
    submit = SubmitField()