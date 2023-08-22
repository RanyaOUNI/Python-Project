from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE_NAME

class Blood_type:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.type = data_dict['type']
	
