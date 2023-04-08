from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField("Login / email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password_again = PasswordField("Password again", validators=[DataRequired()])
    surname = StringField("Surname", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age")
    position = StringField("Position")
    speciality = StringField("Speciality")
    address = StringField("Address")
    submit = SubmitField("Submit")
