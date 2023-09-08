from flask_app.models.hospital import Hospital
from flask_app.models.blood_type import Blood_type
from flask_app.models.donation import Donation
from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.models.user import User
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
        self.user ={}
        self.demand_user={}
        self.donate_user={}
        self.donator_blood = {}
        self.demand_blood = {}

        


    @classmethod
    def create(cls,data_dict):
        query = """INSERT INTO demands 
                    (blood_type_id,user_id, hospital_id, patient_CIN, patient_first_name, patient_last_name,gender)
                    VALUES 
                    (%(blood_type_id)s,%(user_id)s,%(hospital_id)s,%(patient_CIN)s,%(patient_first_name)s,%(patient_last_name)s,%(gender)s);"""
        return MySQLConnection(DATABASE_NAME).query_db(query, data_dict) 

    
    @staticmethod
    def validate(data_dict):
        is_valid = True
        
        if len(data_dict['patient_first_name'])<2:
            is_valid =False
            flash("Name not valid", "patient_first_name")

        if len(data_dict['patient_last_name'])<2:
            is_valid =False
            flash("Name too short", "patient_last_name")

        if len(data_dict["patient_CIN"])!=8:
            is_valid = False
            flash("CIN too short", "patient_CIN")
        
        return is_valid   


        
        

    @classmethod 
    def get_all_demands_with_hospitals(cls,data):
        query = """
                select * from demands
                left join hospitals on hospitals.id = demands.hospital_id
                left join blood_type on blood_type.id = demands.blood_type_id 
                left join donations on donations.id = demands.id
                where demands.user_id !=%(id)s and demands.id not in (select donations.demand_id from donations);
                """
        result = MySQLConnection(DATABASE_NAME).query_db(query,data)
        
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
                'updated_at':row['updated_at'],
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
    
    @classmethod 
    def get_all_demands_of_user(cls,data):
        query = """
                select * from demands
                left join hospitals on hospitals.id = demands.hospital_id
                left join blood_type on blood_type.id = demands.blood_type_id 
                left join donations on donations.id = demands.id
                where demands.user_id =%(id)s;
                """
        result = MySQLConnection(DATABASE_NAME).query_db(query,data)
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
                'updated_at':row['updated_at'],
            }
            demand.donation = Donation(donation)
            demand.hospital = Hospital(hospital)
            demand.blood_type = Blood_type(blood_type)
            demands.append(demand)
        return demands

    @classmethod 
    def get_all_demands_for_hospitals(cls,data):
        query = """
                            select * from demands
            join donations on demands.id = donations.demand_id 
            join users as demands_people on demands_people.id= demands.user_id
            left join blood_type as demander_blood on demander_blood.id = demands_people.blood_type_id
            join users as donations_people on donations_people.id = donations.user_id
            left join blood_type as donator_blood on donator_blood.id = donations_people.blood_type_id
            WHERE demands.hospital_id  = %(id)s;
                """
        result = MySQLConnection(DATABASE_NAME).query_db(query,data)
        demands = []
        print('demmmmaaaaannnddd:', result)
        for row in result:
            print("rooooooow",row)
            demand = cls(row)
            print(demand.__dict__)
            donation = { 
            'id':row['donations.id'],
            'demand_id':row['demand_id'],
            'user_id':row['donations.user_id'],
            'is_confirmed':row['is_confirmed'],
            'created_at':row['donations.created_at'],
            'updated_at':row['updated_at'] 
            }
            user_demands = {
                'id':row['demands_people.id'],
                'blood_type_id':row['demands_people.blood_type_id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'gender':row['demands_people.gender'],
                'email':row['email'],
                'password':row['password'],
                'address':row['address'],
                'date_birth':row['date_birth'],
                'phone':row['phone'],
                'role':row['role'],
                'CIN':row['CIN'],
                'created_at':row['demands_people.created_at'],
                'updated_at':row['demands_people.updated_at'],
            }
            user_donate = { 
            'id':row['donations_people.id'],
            'blood_type_id':row['donations_people.blood_type_id'],
            'first_name':row['donations_people.first_name'],
            'last_name':row['donations_people.last_name'],
            'gender':row['donations_people.gender'],
            'email':row['donations_people.email'],
            'password':row['donations_people.password'],
            'address':row['donations_people.address'],
            'date_birth':row['donations_people.date_birth'],
            'phone':row['donations_people.phone'],
            'role':row['donations_people.role'],
            'CIN':row['donations_people.CIN'],
            'created_at':row['donations_people.created_at'],
            'updated_at':row['donations_people.updated_at'],
        }   
            donator_blood = {
                'id':row['donator_blood.id'],
                'type':row['donator_blood.type']
            }
            demand_blood ={
                'id':row['demander_blood.id'],
                'type':row['type']
            }

            demand.donator_blood = Blood_type(donator_blood)
            demand.demand_blood = Blood_type(demand_blood)
            demand.demand_user = User(user_demands)
            demand.donate_user = User(user_donate)
            demand.donation = Donation(donation)
            demands.append(demand)
        return demands

        