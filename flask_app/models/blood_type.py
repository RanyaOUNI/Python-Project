from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE_NAME

b_comp = {"O+": ['O+', 'A+', 'B+', 'AB+'],
          "A-": ['A-', 'A+', 'AB-', 'AB+'],
          "A+": ['A+', 'AB+'],
          "B-": ['B-', 'B+', 'AB-', 'AB+'],
          "B+": ['B+', 'AB+'],
          "AB+": ['AB+'],
          "AB-": ['AB-', 'AB+'],
          "O-": ["A+", "A-", "B+", "B-", "O-", "O+", "AB+", "AB-"]}

class Blood_type:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.type = data_dict['type']


