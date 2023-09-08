from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.donation import Donation
from flask_app.models.user import User
from flask_app.models.hospital import Hospital






@app.route('/donation')
def donation():
    return render_template('question.html')

@app.route('/donation/donate/<int:demand_id>')
def donate(demand_id):
    logged_user = User.get_by_id({"id": session["user_id"]})
    # hospital_demand = Hospital.get_hospital_of_demand({'demand_id':demand_id})
    data={
        'user_id':logged_user.id,
        'demand_id':demand_id,
        'is_confirmed':1,
        # 'hospital_id':demand.hospital_id
    }
    Donation.create_donation(data)
    return redirect('/user')