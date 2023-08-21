from flask_app.config.mysqlconnection import connectToMySQL
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

    @classmethod
    def create(cls,data_dict):
        query = """INSERT INTO demands 
                    (blood_type_id,user_id, hospital_id, patient_CIN, patient_first_name, patient_last_name,gender)
                    VALUES 
                    (%(blood_type_id)s,%(user_id)s,%(hospital_id)s,%(patient_CIN)s,%(patient_first_name)s,%(patient_last_name)s,%(gender)s);"""
        return connectToMySQL(DATABASE_NAME).query_db(query, data_dict) 

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM recipes
                    JOIN users on recipes.user_id = users.id;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        all_recipes =[]
        for row in results:
            recipe = cls(row)
            recipe.poster = (row['first_name'])
            all_recipes.append(recipe)
        return all_recipes

    # @classmethod
    # def get_by_id(cls,data_dict):
    #     query = """SELECT * FROM recipes WHERE id=%(id)s;"""
    #     result = connectToMySQL(DATABASE).query_db(query, data_dict)
    #     recipe = cls(result[0])
    #     recipe.poster = (result[0]['first_name'])
    #     return recipe   
    @classmethod
    def get_by_id(cls,data_dict):
        query = """SELECT * FROM recipes JOIN users ON recipes.user_id = users.id
                    WHERE recipes.id=%(id)s;"""
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        
        recipe = cls(result[0])
        recipe.poster = f"{result[0]['first_name']}"
        return recipe
    

    @classmethod
    def update(cls,data_dict):
        query= """UPDATE recipes
                SET 
                name= %(name)s, instructions= %(instructions)s,
                under_30min= %(under_30min)s, date_made= %(date_made)s, 
                description= %(description)s
                WHERE id= %(id)s;"""
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)
    
    @classmethod
    def delete(cls,data_dict):
        query= """DELETE FROM recipes WHERE id= %(id)s; """
        return connectToMySQL(DATABASE_NAME).query_db(query,data_dict)


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
