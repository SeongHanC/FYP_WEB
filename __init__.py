from flask import Flask, render_template,flash,request,redirect,url_for,jsonify,session
from pyld import jsonld
import json
import sqlite3
from datetime import datetime
from flask_login import LoginManager,login_user,logout_user,current_user,login_required
from wtforms import Form, BooleanField,StringField,validators
from RegistrationForm import Registration
from DBConnect import connection
from MySQLdb import escape_string as thwart
import gc
import rdflib_search

app = Flask(__name__)
app.secret_key = '\x88\xe4\x18H\xf3> d\x08\xa2\xe9U\r\xfc\xff,\x88\xa8\xe6\x87\x99u\x9b\x84'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def welcome():
    return render_template('welcome_page.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/login',methods=["GET","POST"])
def login():

    # error = ''
    #
    # try:
    #
    #     c, conn = connection()
    #     if request.method == "POST":
    #
    #         data = c.execute("SELECT * FROM users WHERE username = (%s)",
    #                          thwart(request.form['username']))
    #
    #         data = c.fetchone()[2]
    #
    #         if (request.form['passowrd'],data):
    #             session['logged_in'] = True
    #             session['username'] = request.form['username']
    #             flash("Login Successful")
    #             return redirect(url_for(homepage))
    #         else:
    #             error = "Invalid username or password. Please try again"
    #
    #     gc.collect()
    #     return render_template("login.html", error=error)
    #
    # except Exception as e:
    #
    #     error = "Invalid username or password. Please try again"
    #     return render_template("login.html", error=error)

    error = ''

    try:

        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            if attempted_username == "admin" and attempted_password == "admin":
                return redirect(url_for('homepage'))

            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error=error)

    except Exception as e:
        return render_template("login.html", error=error)


@app.route('/register',methods=["GET","POST"])
def register():

    try:
        form = Registration(request.form)

        if request.method == "POST" and form.validate():
            name = form.name.data
            username = form.username.data
            password = form.password.data
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)",
                          (thwart(username)))

            if int(x) > 0:
                flash("Username is already taken. Please choose another username")
                return render_template('register.html', form=form)

            else:
                c.execute("INSERT INTO users (name, username, password) VALUES (%s, %s, %s)",
                          (thwart(name), thwart(username), thwart(password)))

                conn.commit()
                flash("Congrats! You have been registered!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('login'))

        return render_template("register.html", form=form)

    except Exception as e:
        return (str(e))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('welcome'))

@app.route('/event_planner',methods=['GET','POST'])
def event_planner():

    error = ""

    try:

        if request.method == 'POST':
            select_state = request.form.get('state')
            select_et = request.form.get('service')

            if (select_state == 'Selangor' and select_et == 'Music Equipment'):
                return redirect(url_for('result_selangor_musicEQ'))

            elif (select_state == 'Selangor' and select_et == 'PA System'):
                return redirect(url_for('result_selangor_pa_system'))

            elif (select_state == 'Selangor' and select_et == 'Costumes'):
                return redirect(url_for('result_selangor_FNB'))

            elif (select_state == 'Penang' and select_et == 'Food & Beverages'):
                return redirect(url_for('result_pen_costume'))

            else:
                error = "No match found, please find again"

        return render_template("event_planner.html", error=error)

    except Exception as e:
        return render_template("event_planner.html", error=error)



@app.route('/event_finder')
def event_finder():
    return "hello"

@app.route('/result_selangor_musicEQ')
def result_selangor_musicEQ():
    return render_template("ABC_Solution.html")

@app.route('/result_selangor_pa_system')
def result_selangor_pa_system():
    return render_template("ABC_Solution.html")

@app.route('/result_selangor_FNB')
def result_selangor_FNB():
    return render_template("BLA_Sdn_Bhd.html")

@app.route('/result_pen_costume')
def result_pen_costume():
    return render_template("ABC_Solution.html")

if __name__ == '__main__':
    app.run(debug=True)
