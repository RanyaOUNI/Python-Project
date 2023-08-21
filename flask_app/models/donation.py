from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app import DATABASE_NAME




class Donation:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.is_confirmed = data_dict['is_confirmed']
        self.demand_id = data_dict['demand_id']
        self.hospital_id = data_dict['hospital_id']
        self.user_id = data_dict['user_id']
        self.user_blood_type_id = data_dict['user_blood_type_id']
        self.user_donations_id = data_dict['created_at']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        

    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO trips (is_confirmed,user_id,user_blood_type_id) VALUES (%(destination)s,%(start_date)s,%(end_date)s,%(plan)s);
            """
        return MySQLConnection(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM trips;
""" 