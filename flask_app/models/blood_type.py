from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE_NAME


class Blood_type:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.type = data_dict['type']




LoopVar = True
while LoopVar == True:
	DonorBlood, DonorRh = input("What is the donor's blood group? "), input("What is the donor's Rh factor? ")
	PatientBlood, PatientRh = input("What is the patient's blood group? "), input("What is the patient's Rh factor? ")
	NoComp = False
	if DonorBlood != "O" and DonorBlood != PatientBlood and PatientBlood !="AB":
		NoComp = True
	if DonorRh != '-' and PatientRh != DonorRh:
		if NoComp == True:
			print("Both blood group and Rh factor do not match.")
		else:
			print("Rh factors do not match.")
	else:
		if NoComp == True:
			print("Blood groups do not match.")
		else:
			print("Match.")
			LoopVar = False