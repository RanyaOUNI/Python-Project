from flask_app import app
from flask_app.controllers import users
from flask_app.controllers import donations
from flask_app.controllers import demands


# ! Don't forget to import all controllers here 


if __name__ == '__main__':
    app.run(debug=True,port=5000)