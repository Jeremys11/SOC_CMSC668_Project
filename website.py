from flask import Flask, render_template, redirect, url_for, request
import json
import pymysql as pymysql
import pandas as pd
from joblib import dump, load
#from flask_login import LoginManager


#user_database = {"Jeremy":"pass","Bob":"corn"}

##Definition to run this file
app = Flask(__name__)

"""login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)"""


## Homepage
#Button to login goes to login.html
#Button to register goes to register.html
@app.route("/")
def home():
    return render_template("homepage.html")

## URL with /login at end
## "Login Page"
@app.route("/login", methods=['GET', 'POST'])
def login():

    openfile = open('users.json')
    user_database = json.load(openfile)
    openfile.close()

    error = None
    if request.method == 'POST':
        if user_database[request.form['username']] != request.form['password']:
            error = 'Invalid Credentials. Please try again.'
            return render_template("error.html")
        else:
            return redirect(url_for('userhome', username=request.form['username']))

    return render_template('login.html', error=error)

#"Registration Page"
@app.route("/register", methods=['GET', 'POST'])
def register():

    openfile = open('users.json')
    user_database = json.load(openfile)
    openfile.close()
    error = None

    if request.method == 'POST':
        if request.form['username'] in user_database:
            error = 'Invalid Credentials. Please try again.'
            return render_template("error.html")
        else:
            user_database[request.form['username']] = request.form["password"]
            json_object = json.dumps(user_database, indent = 4)
            with open("users.json", "w") as outfile:
                outfile.write(json_object)

            return redirect(url_for('login'))

    return render_template("register.html")

##
##
## USER HOMEPAGE SPECIFIC FOR EACH USER
##
##
@app.route('/user')
def userhome():

    openfile = open('survey.json')
    empty_survey = json.load(openfile)
    openfile.close()
    username = request.args['username']
    #password = request.args['password']
    #return render_template("userhome.html", variable=empty_survey, username=username)
    return render_template("userhome.html", variable=empty_survey, username=username)

@app.route('/results', methods=['GET','POST'])
def results():
    connection=pymysql.connect(host='localhost', user='root', password='mansipatel', db='SOC')
    # name=request.form['name']

    age=request.form['age']#t
    gender=request.form['gender']
    country=request.form['country']#t
    state=request.form['state']#t
    selfemp=request.form['selfemp']
    famhist=request.form['famhist']#t
    treat=request.form['treat']
    workinter=request.form['workinter']
    noemp=request.form['noemp']
    remote=request.form['remote']
    techcomp=request.form['techcomp']
    benefits=request.form['benefits'].replace("'","''")
    care=request.form['care']
    wellprog=request.form['wellprog'].replace("'","''")
    help=request.form['help'].replace("'","''")
    anonymity=request.form['anonymity'].replace("'","''")
    leave=request.form['leave'].replace("'","''")
    menconsequences=request.form['menconsequences']
    phyconsequences=request.form['phyconsequences']
    coworkers=request.form['coworkers']
    supervisor=request.form['supervisor']
    meninterview=request.form['meninterview']
    phyinterview=request.form['phyinterview']
    menvsphy=request.form['menvsphy'].replace("'","''")
    obsconsq=request.form['obsconsq']
    comments=request.form['comments']#t
    print(comments)
    cursor=connection.cursor()
    # INSERT INTO survey (id,Age,Gender,Country,state,self_employed,family_history,treatment,work_interfere,no_employees,remote_work,tech_company,benefits,care_options,seek_help,anonymity,leave1,mental_health_consequence,phys_health_consequence,coworkers,supervisor,mental_health_interview,mental_vs_physical,obs_consequence,comments) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');

    cursor.execute("INSERT INTO survey(Age,Gender,Country,state,self_employed,family_history,treatment,work_interfere,no_employees,remote_work,tech_company,benefits,care_options,wellness_program,seek_help,anonymity,leave1,mental_health_consequence,phys_health_consequence,coworkers,supervisor,mental_health_interview,phys_health_interview,mental_vs_physical,obs_consequence,comments) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(age,gender,country,state,selfemp,famhist,treat,workinter,noemp,remote,techcomp,benefits,care,wellprog,help,anonymity,leave,menconsequences,phyconsequences,coworkers,supervisor,meninterview,phyinterview,menvsphy,obsconsq,comments))
    connection.commit()
    cursor.close()
    connection.close()
    return render_template("results.html")

@app.route('/survey')
def survey():
    return render_template("test_survey.html")

##
##  Company Pages
##
@app.route("/company_login", methods=['GET', 'POST'])
def company_login():

    openfile = open('companies.json')
    company_database = json.load(openfile)
    openfile.close()

    error = None
    if request.method == 'POST':
        if company_database[request.form['username']] != request.form['password']:
            error = 'Invalid Credentials. Please try again.'
            return render_template("error.html")
        else:
            return redirect(url_for('company_home', username=request.form['username']))

    return render_template('company_login.html', error=error)

#"Registration Page"
@app.route("/company_register", methods=['GET', 'POST'])
def company_register():

    openfile = open('companies.json')
    user_database = json.load(openfile)
    openfile.close()
    error = None

    if request.method == 'POST':
        if request.form['username'] in user_database:
            error = 'Invalid Credentials. Please try again.'
            return render_template("error.html")
        else:
            user_database[request.form['username']] = request.form["password"]
            json_object = json.dumps(user_database, indent = 4)
            with open("companies.json", "w") as outfile:
                outfile.write(json_object)

            return redirect(url_for('company_login'))

    return render_template("company_register.html")


@app.route('/company_home')
def company_home():
    username = request.args['username']
    return render_template("company_home.html", variable="1234", username=username)



if __name__ == "__main__":
    app.run(debug=True)
