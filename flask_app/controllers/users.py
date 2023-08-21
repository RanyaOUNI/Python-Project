from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.donation import Donation
from flask_bcrypt import Bcrypt
from flask_app.models.demand import Demand   

bcrypt = Bcrypt(app)



@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("registration_form.html")

@app.route('/user')
def user():
    every_demand = Demand.get_all_demands_with_hospitals()
    print(every_demand[0].hospital)
    return render_template("user.html", every_demand = every_demand)

@app.route('/register2')
def register2():
    return render_template("register2.html")

@app.route('/my_account')
def my_account():
    return render_template("my_account.html")

@app.route('/hospital_dashboard')
def hospital_dashboard():
    return render_template("Hospital.html")

@app.route('/blood_request')
def blood_request():
    every = Demand.get_all_demands_with_hospitals()
    return render_template("blood_request.html",every = every)