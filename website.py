from flask import Flask, render_template, redirect, url_for, request
import json


#user_database = {"Jeremy":"pass","Bob":"corn"}

##Definition to run this file
app = Flask(__name__)

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
    return render_template("userhome.html", variable=empty_survey, username=username)

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