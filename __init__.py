from flask import Flask, render_template,request,redirect,url_for
from pyld import jsonld
import json

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


@app.route('/signup')

def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
