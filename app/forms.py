from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterphonenumberForm(FlaskForm):
    phonenumber = IntegerField('phonenumber', validators=[DataRequired()])
    name = SubmitField('Confirm_phonenumber', validators = [DataRequired(), EqualTo("required")])
    submit = SubmitField()