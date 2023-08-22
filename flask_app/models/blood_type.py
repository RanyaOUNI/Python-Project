from flask_app.config.mysqlconnection import MySQLConnection

b_comp = {
    "O+": ["O+", "A+", "B+", "AB+"],
    "A-": ["A-", "A+", "AB-", "AB+"],
    "A+": ["A+", "AB+"],
    "B-": ["B-", "B+", "AB-", "AB+"],
    "B+": ["B+", "AB+"],
    "AB+": ["AB+"],
    "AB-": ["AB-", "AB+"],
    "O-": ["A+", "A-", "B+", "B-", "O-", "O+", "AB+", "AB-"],
}


class Blood_type:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.type = data_dict["type"]
        self.id = data_dict["id"]
        self.type = data_dict["type"]

    @classmethod
    def get_all():
        pass

    @classmethod
    def get_all_types(cls):
        query = """SELECT * FROM blood_type;"""
        result = MySQLConnection(DATABASE_NAME).query_db(query)
        all_types = []
        for row in result:
            type = cls(row)
            all_types.append(type)
        return all_types
    
    @staticmethod
    def check_compatibility(donor_btype, recipient_btype):
        for blood in b_comp[donor_btype]:
            if blood == recipient_btype:
                return True
            return False
    
    


    # @staticmethod
    # def check_compatibility(donor_btype, recipient_btype):
	# 	Demand.get_all_demands_with_hospitals()
	# 	User.get_users_with_blood_type()
	# 	for blood in b_comp[donor_btype]:
	# 			if blood == recipient_btype:
	# 				return True
	# 		return False


