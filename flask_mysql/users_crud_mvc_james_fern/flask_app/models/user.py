from flask_app.config.mysqlconnection import connectToMySQL
class Model:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO users (first_name, last_name, email) 
            VALUES(%(first_name)s, %(last_name)s, %(email)s);
        """
        return connectToMySQL("users_schema").query_db(query, form_data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            users.append(cls(user) )
        return users
    
    @classmethod
    def get_one(cls,id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_schema').query_db(query, {"id":id})
        if results:
            row=results[0]
            one_user=cls(row)
            return one_user


    @classmethod
    def update (cls, form_data):
        query = """UPDATE users
            SET first_name=%(first_name)s, last_name =%(last_name)s, email = %(email)s 
            WHERE id = %(id)s"""
        return connectToMySQL("users_schema").query_db(query, form_data)

    @classmethod
    def delete(cls, id):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL("users_schema").query_db(query, {"id":id})