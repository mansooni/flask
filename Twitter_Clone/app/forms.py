from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    name = StringField('Full name', validators=[InputRequired('A full name is required'), Length(max=100, message='Your name can\'t be more than 100 characters.')])
    username = StringField('Username', validators=[InputRequired('Username is required'), Length(max=30, message='Your username is too many characters.')])
    password = PasswordField('Password', validators=[InputRequired('A password is required')])
    image = FileField()
