from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friendship_model
class User:
    def __init__( self , data ):
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email_address']
        self.id=data['id']

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO users (first_name, last_name, email_address) 
            VALUES(%(first_name)s, %(last_name)s, %(email)s);
        """
        return connectToMySQL("friendships_schema").query_db(query, form_data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('friendships_schema').query_db(query)
        all_users = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            all_users.append(cls(user))
        return all_users


