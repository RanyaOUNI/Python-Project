from flask_app.config.mysqlconnection import MySQLConnection
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
        result = MySQLConnection(DATABASE_NAME).query_db(query)
        print("******HOSPITALS_WITH_DONA*****",result)
        return []


    # @classmethod 
    # def get_all_hospitals(cls):
    #     query="""
    #     SELECT * FROM hospitals;
    #     """
    #     result = MySQLConnection(DATABASE_NAME).query_db(query)
    #     print(result)
    #     all_hospitals = []
    #     for row in result:
    #         host = cls(row)
    #         all_hospitals.append(host)
    #     return all_hospitals

    # @classmethod
    # def edit_donation(cls,data_dict):
    #     query ="""
    #     UPDATE donations SET is_confirmed = "confirmed" WHERE id =%(id)s;
    #     """
    #     result = MySQLConnection(DATABASE_NAME).query_db(query, data_dict)
    #     return result



    @classmethod
    def get_hospital_by_id(cls, data_dict):
        query = """SELECT * FROM hospitals WHERE id =%(id)s;"""
        result = MySQLConnection(DATABASE_NAME).query_db(query, data_dict)
        # print('RESULT*',result)
        return cls(result[0])



    @classmethod
    def get_hospital_by_email(cls, data_dict):
        query = """SELECT * FROM hospitals WHERE email = %(email)s;"""
        result = MySQLConnection(DATABASE_NAME).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def create_hospital(cls, data_dict):
        query = """INSERT INTO hospitals (name, address, email, password) VALUES (%(name)s,%(address)s,%(email)s,%(password)s);"""
        return MySQLConnection(DATABASE_NAME).query_db(query, data_dict)
    @classmethod
    def get_all_hospitals(cls):
        query="""
        SELECT * FROM hospitals;"""
        result = MySQLConnection(DATABASE_NAME).query_db(query)
        print(result)
        all_hospitals = []
        for row in result:
            host = cls(row)
            all_hospitals.append(host)
        return all_hospitals
    
    @classmethod
    def destroy_hospital(cls, data_dict):
        query ="""DELETE FROM hospitals WHERE id= %(id)s;"""
        return MySQLConnection(DATABASE_NAME).query_db(query,data_dict)