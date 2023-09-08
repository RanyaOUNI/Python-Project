from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.blood_type import Blood_type
from flask_app.models.demand import Demand
from flask_app.models.hospital import Hospital
from flask_app.models.donation import Donation
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)



# !CRUD Hospital----!

@app.route("/admin")
def admin():
    all_hospitals= Hospital.get_all_hospitals()
    all_donations = Donation.get_all()
    show_all= User.get_all_users()
    
    return render_template("admin.html",all_donations=all_donations, all_hospitals= all_hospitals,show_all=show_all)


# ----------CREATE--------
@app.route("/create_hospital")
def hospital():
    return render_template("creation_hospital.html")

@app.route('/create_hospital', methods=['POST'])
def create_hospital():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data_dict = {
            **request.form,
            'password':pw_hash
        }
        
    Hospital.create_hospital(data_dict)
    
        
    return redirect('/admin')

# ---------DELETE-------------

@app.route('/admin/<int:hospital_id>/destroy', methods=['POST'])
def destroy(hospital_id):
    Hospital.destroy_hospital({'id':hospital_id})
    return redirect('/admin')






# !Donor----!

@app.route('/admin/<int:donation_id>/destroy_donation',methods=['POST'])
def destroy_donation(donation_id):
    Donation.delete({'id':donation_id})
    return redirect('/admin')


@app.route('/admin/<int:user_id>/destroy_user',methods=['POST'])
def destroy_user(user_id):
    User.destroy_user({'id':user_id})
    return redirect('/admin')



