from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):

    Name = StringField('Name', [validators.Length(min=2, max=25)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])