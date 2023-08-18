from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE


import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Demand:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.blood_type_id= data_dict['blood_type_id']
        self.hospital_id = data_dict['hospital_id']
        self.user_id = data_dict['user_id']
        self.patient_CIN = data_dict['patient_CIN']
        self.patient_first_name = data_dict['patient_first_name']
        self.patient_last_name = data_dict['patient_last_name']
        self.gender = data_dict['gender']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
