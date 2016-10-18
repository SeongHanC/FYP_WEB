from flask_wtf import Form
from wtforms import StringField,PasswordField,validators,IntegerField,BooleanField

class Registration(Form):

    username = StringField('Username', [validators.Length(min=4, max=25)])

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])


    confirm = PasswordField('Repeat Password')

    state = StringField('State', [validators.Length(min=4, max=25)])

    location = StringField('Location', [validators.Length(min=4, max=25)])

    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice', [validators.DataRequired()])