from flask_app import DATABASE
from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash




import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile('\d.*[A-Z]|[A-Z].*\d')

class User :
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.blood_type_id = ['blood_type_id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.email = data_dict['email']
        self.password = data_dict['password']
        self.role = data_dict['role']
        self.phone = data_dict['phone']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.CIN = data_dict['CIN']
        self.donation_id = data_dict['donation_id']