from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app import DATABASE_NAME





# @classmethod
# def destroy_hospital(cls,data_dict):
#     query="""DELETE FROM hospitals WHERE id= %(id)s;"""
#     return MySQLConnection(DATABASE_NAME).query_db(query,data_dict)