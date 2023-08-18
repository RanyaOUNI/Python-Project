from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE


import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Donation:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.is_confirmed = data_dict['is_confirmed']
        self.demand_id = data_dict['demand_id']
        self.user_id = data_dict['user_id']
        self.user_blood_type_id = data_dict['user_blood_type_id']
        self.user_donations_id = data_dict['created_at']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
