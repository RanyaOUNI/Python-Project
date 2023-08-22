from flask_app import DATABASE_NAME
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
        

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users 
                    (first_name, last_name, email, password)
                    VALUES 
                    (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        print("***********not*********")
        return MySQLConnection(DATABASE_NAME).query_db(query, data_dict)
    
    # @classmethod
    # def get_by_id(cls, data_dict):
    #     query = """SELECT * FROM users WHERE id =%(id)s;"""
    #     result = MySQLConnection(DATABASE_NAME).query_db(query, data_dict)
    #     return cls(result[0])
    

    @classmethod
    def get_users_with_blood_type(cls):
        query ="""
        SELECT * FROM USERS 
        LEFT JOIN blood_type 
        ON users.blood_type_id = blood_type.id ;
"""
        result = MySQLConnection(DATABASE_NAME).query_db(query)
        return result
        


    @classmethod
    def get_by_email(cls, data_dict):
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        result =MySQLConnection(DATABASE_NAME).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False
    


    @staticmethod
    def validate_register(data_dict):
        is_valid = True
        if len( data_dict['first_name'])< 2:
            print("First Name too short .....")
            flash("First Name too short .....", "first_name")
            is_valid = False
        if len(data_dict['last_name'])< 2:
            print("Last Name too short .....")
            flash("Last Name too short .....", "last_name")
            is_valid = False
        if len(data_dict['password'])< 7:
            print("Password too short .....")
            flash("Password too short .....", "password")
            is_valid = False
        if data_dict['password'] != data_dict['confirm_password']:
            print("Password and Confirm password Don't match !!!!!")
            flash("Password and Confirm password Don't match !!!!!", "confirm_password",)
            is_valid = False
        if not EMAIL_REGEX.match(data_dict['email']): 
            flash("Invalid email address!","email")
            is_valid = False
        elif User.get_by_email({'email':data_dict['email']}):
            flash("Email Already taken . Hope by you !!!! ", "email")
            is_valid = False
        return is_valid


   
