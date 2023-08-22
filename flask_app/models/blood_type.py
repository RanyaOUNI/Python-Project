from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE_NAME

b_comp = {"O+": ['O+', 'A+', 'B+', 'AB+'],
          "A-": ['A-', 'A+', 'AB-', 'AB+'],
          "A+": ['A+', 'AB+'],
          "B-": ['B-', 'B+', 'AB-', 'AB+'],
          "B+": ['B+', 'AB+'],
          "AB+": ['AB+'],
          "AB-": ['AB-', 'AB+'],
          "O-": ["A+", "A-", "B+", "B-", "O-", "O+", "AB+", "AB-"]}

class Blood_type:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.type = data_dict['type']




	@staticmethod
	def check_compatibility(donor_btype, recipient_btype):
		for blood in b_comp[donor_btype]:
			if blood == recipient_btype:
				return True
		return False

    # def get_blood_compatibility():
    #   while True:
    #     donor_blood_type = input("What is donor's blood type?: ").upper()
    #     receiver_blood_type = input("What is receiver's blood type?: ").upper()

    #     if donor_blood_type not in blood_type or receiver_blood_type not in blood_type:
    #         print("Invalid blood type. O-, O+, A-, A+, B-, B+, AB-, AB+ are the only blood types available.")
    #     else:
    #         break
      

    #   compatibility = False

      if donor_blood_type == 'O-':
           compatibility = True
      elif donor_blood_type == 'O+':
        if receiver_blood_type in ['O+', 'A+', 'B+', 'AB+']:
            compatibility = True
      elif donor_blood_type == 'A-':
        if receiver_blood_type in ['A-', 'A+', 'AB-', 'AB+']:
            compatibility = True
      elif donor_blood_type == 'A+':
        if receiver_blood_type in ['A+', 'AB+']:
            compatibility = True
      elif donor_blood_type == 'B-':
        if receiver_blood_type in ['B-', 'B+', 'AB-', 'AB+']:
            compatibility = True
      elif donor_blood_type == 'B+':
        if receiver_blood_type in ['B+', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'AB-':
        if receiver_blood_type in ['AB-', 'AB+']:
            compatibility = True
    elif donor_blood_type == 'AB+':
        if receiver_blood_type in ['AB+']:
            compatibility = True

    if compatibility:
        print("Donor is compatible with receiver.")
    else:
        print("Donor is not compatible with receiver. Dangerous immunological reaction may occur if transfusion takes place.")

    get_blood_compatibility()

disclaimer = "This script is for educational purposes only and clinical correlation is required!"
print(disclaimer)