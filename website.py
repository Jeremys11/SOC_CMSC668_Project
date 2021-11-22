from flask import Flask
#import flask_login
from flask import render_template
#from tinydb import TinyDB, Query
#from database import DatabaseQueries

##Definition to run this file
app = Flask(__name__)

## Homepage
@app.route("/")
def home():
    #Button to login goes to login.html
    #Button to register goes to register.html
    return render_template("homepage.html")

## URL with /login at end
## "Login Page"
@app.route("/login")
def login():
    #Views login API
    #Test login message -- acces {{login_message}} in HTML file
    login_message = "Login Message Test"
    return render_template('login.html', login_message=login_message)

#"Registration Page"
@app.route("/register")
def register():
    #Views signup API
    #Take username and password
    #Allow button to return to homepage
    return render_template("register.html")

##
##
## USER HOMEPAGE SPECIFIC FOR EACH USER
##
##
@app.route('/user/<username>')
def userhome(username):
    return render_template("userhome.html")
    
if __name__ == "__main__":
    app.run(debug=True)