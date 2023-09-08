from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.donation import Donation
from flask_app.models.user import User
from flask_app.models.blood_type import Blood_type
from flask_bcrypt import Bcrypt
from flask_app.models.demand import Demand
from flask_app.models.hospital import Hospital

bcrypt = Bcrypt(app)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/")


@app.route("/login")
def form_register():
    return render_template("login.html")



# @app.route("/user")
# def dashboard():
#     if "user_id" not in session:
#         return redirect("/home.html")
#     logged_user = User.get_by_id({"id": session["user_id"]})
#     return render_template("user.html", user=logged_user)


@app.route("/register", methods=["POST"])
def register():
    if User.validate_register(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form["password"])
        # print("Password : ", request.form["password"])
        # print("Hashed Password : ", pw_hash)
        data_dict = {**request.form, "password": pw_hash}
        user_id = User.create(data_dict)
        session["user_id"] = user_id
        return redirect("/second_register")
    return redirect("/register")






@app.route("/user")
def user():
    
    if "user_id" not in session:
        return redirect("/home")
    logged_user = User.get_by_id({"id": session["user_id"]})
    every_demand = Demand.get_all_demands_with_hospitals({'id':logged_user.id})
    user_demand = Demand.get_all_demands_of_user({'id':logged_user.id})
    return render_template("user.html", every_demand=every_demand, user_demand = user_demand, logged_user = logged_user)

@app.route("/second_register")
def form11():
    all_blood = Blood_type.get_all_types()
    return render_template("register2.html", all_blood=all_blood)






@app.route("/process_register2", methods=["POST"])
def register2():
    data_dict = {**request.form, "id": session["user_id"]}
    if request.form['role'] == "admin":
        User.update(data_dict)
        return redirect('/admin')
    if request.form['role'] == "user":
        User.update(data_dict)
        return redirect('/user')
    # if request.form['role'] == "hospital":
    #     User.update(data_dict)
    #     return redirect('/hospital_dashboard')
    # User.update(data_dict)
    return redirect("/user")



@app.route("/my_account")
def my_account():
    logged_user = User.get_by_id({"id": session["user_id"]})
    print('****************',User.get_by_id({"id": session["user_id"]}))
    blood = User.get_users_with_blood_type({"id": logged_user.id})
    every = Blood_type.get_all_types()
    return render_template("my_account.html", logged_user=logged_user, blood = blood , every = every)



@app.route("/blood_request")
def blood_request():
    every = Blood_type.get_all_types()
    all_hospitals = Hospital.get_all_hospitals()
    return render_template("blood_request.html", every=every,all_hospitals=all_hospitals)


@app.route("/register")
def form():
    return render_template("register.html")

