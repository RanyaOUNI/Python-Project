from flask_app.models.hospital import Hospital
from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app import DATABASE_NAME




class Donation:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.is_confirmed = data_dict['is_confirmed']
        self.demand_id = data_dict['demand_id']
        self.user_id = data_dict['user_id']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.user_name = ""
        self.patient =""
        self.email=""
        self.user_number=0
        self.blood_type=""


    @classmethod 
    def create(cls , data_dict):
        query = """
            INSERT INTO donations (user_id,demand_id) VALUES (%(user_id)s,%(demand_id)s);
            """
        
        results =  MySQLConnection(DATABASE_NAME).query_db(query,data_dict)
        
        return results
    
    @classmethod
    def get_all(cls):
        query="""
        SELECT * FROM donations join users on users.id =donations.user_id
        join demands on demands.id = donations.demand_id
        join blood_type on blood_type.id = users.blood_type_id;""" 
        result = MySQLConnection(DATABASE_NAME).query_db(query)
        all_donations = []
        for row in result:
            donation = cls(row)
            donation.user_name = row['first_name'] + " " + row['last_name']
            donation.user_number = row['phone']
            donation.patient = row['patient_first_name'] + " " + row['patient_last_name']
            donation.email = row['email']
            donation.blood_type= row['type']
            all_donations.append(donation)
        return all_donations

    # @classmethod 
    # def create(cls , data_dict):
    #     query = """
    #         INSERT INTO donations (demand_id,hospital_id,user_id,is_confirmed) VALUES (%(demand_id)s,%(hospital_id)s,%(user_id)s,%(is_confirmed)s);
    #         """
    #     return MySQLConnection(DATABASE_NAME).query_db(query,data_dict)



    @classmethod
    def create_donation(cls,data):
        query="""insert into donations (demand_id,user_id,is_confirmed)
                    values(%(demand_id)s,%(user_id)s,%(is_confirmed)s);"""
        return MySQLConnection(DATABASE_NAME).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query="""delete from donations where id=%(id)s;"""
        return MySQLConnection(DATABASE_NAME).query_db(query,data)



