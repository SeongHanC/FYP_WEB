from flask_wtf import Form
from wtforms import StringField,PasswordField,validators,IntegerField,BooleanField

class Registration(Form):

    name = StringField('Name',[validators.Length(min=2, max=50)])

    username = StringField('Username', [validators.Length(min=4, max=25)])

    email = StringField('Email Address', [validators.Length(min=6, max=35)])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice', [validators.DataRequired()])
