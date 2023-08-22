from flask_app import app
from flask import render_template , request, redirect,session, flash
from flask_app.models.user import User

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/login')
def login():
    print(request.form)
    user_from_db = User.get_by_email({'email':request.form['email']})
    print(user_from_db)
    if user_from_db:
        if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
            # if we get False after checking the password
            flash("Wrong Password !!!","login")
            return redirect('/home.html')
        session['user_id'] = user_from_db.id
        return redirect('/login.html')
    flash("Wrong email !!!!","login")
    return redirect('/home.html')


@app.route('/user_dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/home.html')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("login.html",logged_user=user)

@app.route('/register', methods=["POST"])
def register():
    print('*****REG************',request.form)
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

@app.route('/user')
def user():
    if 'user_id' not in session:
        return redirect('/home.html')
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("user.html")

@app.route('/register2')
def register2():
    return render_template("register2.html")




@app.route('/my_account')
def my_account():
    return render_template("my_account.html")



@app.route('/register')
def form_register():
    return render_template("register.html")

