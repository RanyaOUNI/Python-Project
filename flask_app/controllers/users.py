from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.donation import Donation
from flask_app.models.user import User
from flask_app.models.hospital import Hospital
from flask_app.models.blood_type import Blood_type

from flask_bcrypt import Bcrypt
from flask_app.models.demand import Demand   

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login')
def form_register():
    return render_template("login.html")


@app.route('/login', methods = ['POST'])
def login():
    print(request.form)
    user_from_db = User.get_by_email({'email':request.form['email']})
    print(user_from_db)
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            # if we get False after checking the password
            flash("Wrong Password !!!","login")
            return redirect('/user.html')
        session['user_id'] = user_from_db.id
        return redirect('/user.html')
    flash("Wrong email !!!!","login")
    return redirect('/login')

# @app.route('/user')
# def dashboard():
    # if 'user_id' not in session:
    #     return redirect('/home.html')
    # logged_user = User.get_by_id({'id':session['user_id']})
#     return render_template("login.html",user=logged_user)








@app.route('/register', methods=["POST"])
def register():
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print("Password : ", request.form['password'])
        print("Hashed Password : ", pw_hash)
        data_dict = {
            **request.form,
            'password':pw_hash
        }
        user_id = User.create(data_dict)
        session['user_id'] = user_id
        return redirect('/register2')
    return redirect('/register')



@app.route('/register_page')
def form():
    return render_template("register.html")



@app.route('/user')
def user():
    every_demand = Demand.get_all_demands_with_hospitals()
    print(every_demand[0].hospital)
    Hospital.get_hospital_with_donations()

    return render_template("user.html", every_demand = every_demand)

@app.route('/register2' ,methods =['POST'])
def register2():
    all_blood = Demand.get_all_demands_with_hospitals()
    return render_template("register2.html",all_blood = all_blood)

# @app.route('/register2', methods=["POST"])
# def register2():
#     if User.validate_register(request.form):
#         user_id = User.create(data_dict)
#         session['user_id'] = user_id
#         return redirect('/user.html')
#     return redirect('/register2')


@app.route('/my_account')
def my_account():
    return render_template("my_account.html")

@app.route('/hospital_dashboard')
def hospital_dashboard():
    all = Demand.get_all_demands_with_hospitals()
    return render_template("Hospital.html",all=all)


@app.route('/blood_request')
def blood_request():
    every = Demand.get_all_demands_with_hospitals()
    return render_template("blood_request.html",every = every)