from flask import Flask, render_template,request,redirect,url_for
from pyld import jsonld
import json
import RegisterClass

app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template('homepage.html')

@app.route('/login',methods=["GET","POST"])

def login():

    error = None
    if request.method == 'POST':

        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'

        else:
            return redirect(url_for('homepage'))

    return render_template('login.html', error=error)


@app.route('/register')

def register():

    form = RegisterClass.RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():

        '''
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        '''
        return redirect(url_for('homepage'))

    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
