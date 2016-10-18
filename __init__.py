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
#from rdflib_search import get_types,get_states
import rdflib_search
from rdflib import Graph,Namespace,RDF
import MySQLdb

app = Flask(__name__)
app.secret_key = '\x88\xe4\x18H\xf3> d\x08\xa2\xe9U\r\xfc\xff,\x88\xa8\xe6\x87\x99u\x9b\x84'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.route('/')
def welcome():
    return render_template('welcome_page.html')

@app.route('/homepage',methods=["GET","POST"])
def homepage():

    service_list = get_types()
    states_list = get_states()
    services = remove_duplicates(service_list)
    states = remove_duplicates(states_list)
    error = ""

    try:

        if request.method == 'POST':
            select_state = request.form.get('state')
            select_et = request.form.get('service')

            if select_et == "Concert" and select_state == "Selangor":

                co_name = "BLM Music Solution"
                location = "69, Jalan USJ 8"
                state = "Selangor"
                items = "Music Equipment (Guitar, Violin, etc), PA System"

                for item in get_states():
                    if item == select_state:
                        hist_list_state.append(item)
                        break

                for item1 in get_types():
                    if item1 == select_et:
                        hist_list_service.append(item1)
                        break

                return render_template("result.html", co_name=co_name, state=state, location=location, items=items,
                                       error=error, states=states, services=services)

            elif select_et == "Costumes" and select_state == "Pulau Pinang":

                co_name = "Ian Costumes Factory"
                location = "12, Jalan PP, Gelugor"
                state = "Pulau Pinang"
                items = "All types of costumes (Halloween costumes, party costumes, etc)"

                for item in get_states():
                    if item == select_state:
                        hist_list_state.append(item)
                        break

                for item1 in get_types():
                    if item1 == select_et:
                        hist_list_service.append(item1)
                        break

                return render_template("result.html", co_name=co_name, state=state, location=location, items=items,
                                        error=error,states=states,services=services)

            elif select_et == "Festival" and select_state == "Selangor":

                co_name = "Adi's Fireworks Solution"
                location = "9, Jalan Dato Huri 11, Damansara Utama"
                state = "Selangor"
                items = "Fireworks for festivals, celebration, etc."

                for item in get_states():
                    if item == select_state:
                        hist_list_state.append(item)
                        break

                for item1 in get_types():
                    if item1 == select_et:
                        hist_list_service.append(item1)
                        break

                return render_template("result.html", co_name=co_name, state=state, location=location, items=items,
                                       error=error, states=states, services=services)

            elif select_et == "Food & Beverage" and select_state == "Perak":

                co_name = "Ho Jiak Catering"
                location = "11, Jalan Perak 89"
                state = "Perak"
                items = "Catering (Western, Malay, Chinese, Indian, Fusion)"

                for item in get_states():
                    if item == select_state:
                        hist_list_state.append(item)
                        break

                for item1 in get_types():
                    if item1 == select_et:
                        hist_list_service.append(item1)
                        break

                return render_template("result.html", co_name=co_name, state=state, location=location, items=items,
                                       error=error, states=states, services=services)

            elif select_et == "Music Equipment":

                if select_state == "Melaka":

                    co_name = "Nigel's"
                    location = "25, Jalan Selamat"
                    state = "Melaka"
                    items = "Music Instruments rental services."

                    for item in get_states():
                        if item == select_state:
                            hist_list_state.append(item)
                            break

                    for item1 in get_types():
                        if item1 == select_et:
                            hist_list_service.append(item1)
                            break

                    return render_template("result.html", co_name=co_name, state=state, location=location, items=items,
                                       error=error, states=states, services=services)

                elif select_state == "Selangor":

                    co_name = "BLM Music Solution"
                    location = "69, Jalan USJ 8"
                    state = "Selangor"
                    items = "Music Equipment (Guitar, Violin, etc), PA System"

                    for item in get_states():
                        if item == select_state:
                            hist_list_state.append(item)
                            break

                    for item1 in get_types():
                        if item1 == select_et:
                            hist_list_service.append(item1)
                            break

                    return render_template("result.html", co_name=co_name, state=state, location=location, items=items,
                                           error=error, states=states, services=services)

            elif select_et == "Photography" and select_state == "Johor":

                co_name = "Bean's Photography & Studio"
                location = "19, Jalan Johor Selatan"
                state = "Johor"
                items = "Camera, Camera parts, Photography service for all occasions."

                for item in get_states():
                    if item == select_state:
                        hist_list_state.append(item)
                        break

                for item1 in get_types():
                    if item1 == select_et:
                        hist_list_service.append(item1)
                        break

                return render_template("result.html", co_name=co_name, state=state, location=location, items=items,
                                       error=error, states=states, services=services)

            elif select_et == "Venue" and select_state == "Kuala Lumpur":

                for item in get_states():
                    if item == select_state:
                        hist_list_state.append(item)
                        break

                for item1 in get_types():
                    if item1 == select_et:
                        hist_list_service.append(item1)
                        break

                return render_template("result1.html",error=error, states=states, services=services)

            else:
                error = "No match found. Please try again."

        return render_template("homepage.html", error=error,states=states,services=services)

    except Exception as e:
        return render_template("homepage.html", error=error,states=states,services=services)

@app.route('/login',methods=["GET","POST"])
def login():

    error = ''

    try:

        if request.method == "POST":

            attempted_username = request.form['username']
            attempted_password = request.form['password']

            if attempted_username == "edward" and attempted_password == "admin":
                return redirect(url_for('homepage'))

            else:
                error = "Invalid credentials. Try Again."

        return render_template("login.html", error=error)

    except Exception as e:
        return render_template("login.html", error=error)


@app.route('/register',methods=["GET","POST"])
def register():

    error = ""
    message = ""

    try:
        form = Registration(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            password = form.password.data
            state = form.state.data
            location = form.location.data
            c, conn = connection()

            x = c.execute("SELECT * FROM USERS WHERE USERNAME = ('%s')" % \
                          (username))


            if int(x) > 0:
                error = "Username is already taken. Please choose another username"
                return render_template('register.html', form=form,error = error)

            else:
                c.execute("INSERT INTO USERS (USERNAME, PASSWORD, STATE, LOCATION) VALUES ('%s', '%s', '%s'','%s')" % \
                          (username,password,state,location))

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


@app.route('/user_profile')
def user_profile():

    username = "Edward"

    output_state = []
    output_service = []

    for state in hist_list_state:
        output_state.append(state)

    for serv in hist_list_service:
        output_service.append(serv)

    return render_template("user_profile.html",username=username,states = output_state,services = output_service)

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user="root", passwd="t1213121", db="User")
    cursor = db.cursor()

    g = Graph()
    g.parse("rdf_output.owl")

    hist_list_state = []
    hist_list_service = []

    my_namespace = Namespace("http://www.semanticweb.org/seonghan/ontologies/2016/7/untitled-ontology-3#")


    # rdflib (get all the information from rdf ontology/owl file
    def get_co_name():

        co_name = []

        for name in g.subjects(RDF.type, my_namespace.Event_suppliers):
            co_name.append(g.value(name, my_namespace.ES_Name).toPython())

        return co_name


    def get_types():

        types = []

        for type in g.subjects(RDF.type, my_namespace.Event_suppliers):
            types.append(g.value(type, my_namespace.ES_Type).toPython())

        return types


    def get_states():

        states = []

        for state in g.subjects(RDF.type, my_namespace.Event_suppliers):
            states.append(g.value(state, my_namespace.ES_State).toPython())

        states.sort()
        return states


    def get_loc():

        loc = []

        for location in g.subjects(RDF.type, my_namespace.Event_suppliers):
            loc.append(g.value(location, my_namespace.ES_Location).toPython())

        return loc


    def get_items():

        items = []

        for item in g.subjects(RDF.type, my_namespace.Event_suppliers):
            items.append(g.value(item, my_namespace.ES_Items).toPython())

        items.sort()

        return items

    def remove_duplicates(a_list):

        seen = set()
        output_list = []

        for i in a_list:
            if i not in seen:
                output_list.append(i)
                seen.add(i)

        return output_list


    app.run(debug=True)
