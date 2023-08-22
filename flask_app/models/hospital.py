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
        self.donations = []

    @classmethod
    def get_hospital_with_donations(cls):
        query = """
        SELECT * FROM hospitals
        LEFT JOIN donations ON donations.hospital_id = hospitals.id
        LEFT JOIN demands ON demands.id = donations.demand_id
        LEFT JOIN blood_type ON blood_type_id = blood_type.id;
        """
        result = connectToMySQL(DATABASE_NAME).query_db(query)
        print("******HOSPITALS_WITH_DONA*****",result)
        return []





