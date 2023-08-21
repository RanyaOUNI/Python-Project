from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.donation import Donation






@app.route('/donation')
def donation():
    return render_template('question.html')