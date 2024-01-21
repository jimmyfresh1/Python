from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO dojos (name) 
            VALUES(%(name)s);
        """
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, form_data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

