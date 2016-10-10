from flask_wtf import Form
from wtforms import StringField,PasswordField,validators,IntegerField

class RegisterForm(Form):

    username = StringField('Username', validators.DataRequired([validators.Length(min=4, max=25)]))

    age = IntegerField('Age',validators.DataRequired([validators.Length(min=1,max=3)]))

    email = StringField('Email Address', validators.DataRequired([validators.Length(min=6, max=35)]))

    password = PasswordField('New Password', validators.DataRequired([
        validators.DataRequired(),
        validators.EqualTo('password_confirm', message='Password does not matched')
    ]))

    password_confirm = PasswordField('Repeat Password')

    state = StringField('State', validators.DataRequired([validators.Length(min=6, max=35)]))