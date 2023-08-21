from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE_NAME



class Hospital:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.address = data_dict['address']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
