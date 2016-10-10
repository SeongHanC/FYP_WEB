from flask import Flask, render_template,request,redirect,url_for,jsonify,session
from pyld import jsonld
import json
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
db = SQLAlchemy()
app.secret_key = '\x88\xe4\x18H\xf3> d\x08\xa2\xe9U\r\xfc\xff,\x88\xa8\xe6\x87\x99u\x9b\x84'
app.database = "user.db"

@app.route('/')
def welcome():
    return render_template('welcome_page.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/login',methods=["GET","POST"])
def login():

    error = None
    if request.method == 'POST':

        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'

        else:
            session['logged_in'] = True
            return redirect(url_for('homepage'))

    return render_template('login.html', error=error)


@app.route('/register',methods=["POST"])
def register():
    return("Hello")

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
