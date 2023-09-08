from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.controllers.demands import Demand
from flask_app.controllers.users import User
from flask_app.controllers.donations import Donation
from flask_app.models.hospital import Hospital
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)






# @app.route("/hospital_dashboard")
# def hospital_dashboard():
#     logged_user = User.get_by_id({"id": session["user_id"]})
#     table = Demand.get_all_demands_for_hospitals({"id": logged_user.id})

#     return render_template("Hospital.html", table = table)


@app.route("/hospital_dashboard")
def hospital_dashboard():
    if "hospital_id" not in session:
        return redirect("/login")
    logged_hospital = Hospital.get_hospital_by_id({"id": session["hospital_id"]})
    table = Demand.get_all_demands_for_hospitals({"id": logged_hospital.id})
    print("HOSPITAL_ID*",session["hospital_id"])
    return render_template("Hospital.html" ,hospital=logged_hospital, table = table)


@app.route("/hospital_update", methods=['POST'])
def hospital_update():

    Hospital.edit_donation({'id':request.form['donation_id']})
    return redirect("/hospital_dashboard")
    


@app.route("/login", methods=["POST"])
def login():
    print(request.form)
    user_from_db = User.get_by_email({"email": request.form["email"]})

    if user_from_db:
        if not bcrypt.check_password_hash(
            user_from_db.password, request.form["password"]
        ):
            # if we get False after checking the password
            flash("Wrong Password !!!", "login")
            return redirect("/login")
        if user_from_db.role == "admin":
            return redirect('/admin')
        session["user_id"] = user_from_db.id
        return redirect("/user")

    else:
            hospital_from_db = Hospital.get_hospital_by_email({"email": request.form["email"]})
            if hospital_from_db:
                if not bcrypt.check_password_hash(
            hospital_from_db.password, request.form["password"]
        ):
                # if hospital_from_db.password != request.form["password"]:
                    flash("Wrong credential !!!!", "login")
                    return redirect("/login")
                
                session["hospital_id"] = hospital_from_db.id
                return redirect("/hospital_dashboard")

