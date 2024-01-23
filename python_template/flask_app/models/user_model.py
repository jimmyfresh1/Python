

@staticmethod
    
    if len(user['password']) <3:
    flash ("Password must be at least 3 characters.", "login")
    is valid=False

@classmethod
def check_database(cls,data):
    query="SELECT * FROM users WHERE email= %(email)s"
    results = connectToMySQL(DB).query_db(query,data)
    return results

@classmethod
def get_user_by_id(cls,data):
    query = "SELECT * FROM users WHERE id = %(user_id)s"
    result = connectToMySql(DB).query_db(query,data)
    return cls(result[0])

