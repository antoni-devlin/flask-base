from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

class LoginForm(FlaskForm):
    username = TextField('Username')
    password = PasswordField('Password')
