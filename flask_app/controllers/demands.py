from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.demand import Demand
from flask import flash







@app.route('/demand/create', methods= ['POST'])
def create_demand():
    print("**************"*20,request.form)
    data = {
        **request.form,
        'user_id':session['user_id'],
    }
    Demand.create_demand(data)
    
    return redirect('/user')
