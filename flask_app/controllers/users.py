from flask_app import app
from flask import render_template , request, redirect,session, flash

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template("home.html")
@app.route('/sign in')
def sign():
    return render_template("registration_form")