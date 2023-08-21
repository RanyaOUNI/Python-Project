from flask_app.models.hospital import Hospital
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
        self.created_at = data_dict['created_at']
        self.updated_At = data_dict['updated_At']
        self.hospital = {}
        self.demand={}
        self.donation= {}
        


    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO donations (user_id,demand_id,hospital_id) VALUES (%(user_id)s,%(demand_id)s,%(hospital_id)s);
            """
        
        results =  MySQLConnection(DATABASE_NAME).query_db(query,data_dict)
        print (results)
        return results
    
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM donations  JOIN blood_type ;
""" 
        result = MySQLConnection(DATABASE_NAME).query_db(query)
        all_donations = []
        for row in result:
            donation = cls(row)
            all_donations.append(donation)
        return all_donations
    
    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO donations (demand_id,hospital_id,user_id,is_confirmed) VALUES (%(demand_id)s,%(hospital_id)s,%(user_id)s,%(is_confirmed)s);
            """
        return MySQLConnection(DATABASE_NAME).query_db(query,data_dict)