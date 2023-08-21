from flask_app.models.hospital import Hospital
from flask_app.models.blood_type import Blood_type
from flask_app.models.donation import Donation
from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app import DATABASE_NAME



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
        self.hospital = {}
        self.blood_type = {}
        self.donation= {}

        
        

    @classmethod 
    def get_all_demands_with_hospitals(cls):
            query = """
select * from demands
left join hospitals on hospitals.id = demands.hospital_id
left join blood_type on blood_type.id = demands.blood_type_id 
left join donations on donations.id = demands.id;
"""     
            result = MySQLConnection(DATABASE_NAME).query_db(query)
            print(result)
            demands = []
            for row in result:
                demand = cls(row)
                hospital = { 
                'id':row['hospitals.id'],
                'name':row['name'],
                'address':row['address'],
                'email':row['email'],
                'password':row['password'],
                'created_at':row['hospitals.created_at'],
                'updated_at':row['updated_at']
            }   
                blood_type = {
                    'id':row['blood_type.id'],
                    'type':row['type'],
                }
                donation = {
                    'id':row['id'],
                    'demand_id':row['demand_id'],
                    'hospital_id':row['hospital_id'],
                    'user_id':row['user_id'],
                    'is_confirmed':row['is_confirmed'],
                    'created_at':row['created_at'],
                    'updated_At':row['updated_At'],
                }
                demand.donation = Donation(donation)
                demand.hospital = Hospital(hospital)
                demand.blood_type = Blood_type(blood_type)
                demands.append(demand)
            return demands


    @classmethod
    def create_demand(cls,data_dict):
        query = """
    INSERT INTO demands (blood_type_id,user_id,hospital_id,patient_CIN,patient_first_name,gender,patient_last_name) VALUES (%(blood_type_id)s,%(user_id)s,%(hospital_id)s,%(patient_CIN)s,%(patient_first_name)s,%(gender)s,%(patient_last_name)s);
        """
        result = MySQLConnection(DATABASE_NAME).query_db(query,data_dict)
        return result