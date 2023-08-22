from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.demand import Demand







@app.route('/demand/create', methods= ['POST'])
def create_demand():
    print("**************"*20,request.form)
    Demand.create_demand(request.form)
    
    return redirect('/dashbord')
