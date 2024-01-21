from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo_model import Dojo


class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
            VALUES(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, form_data)
    
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM ninjas;"
    #     results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
    #     ninjas = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for ninja in results:
    #         ninjas.append(cls(ninja) )
    #     return ninjas
    
    @classmethod
    def get_all_in_dojo(cls,id):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id=dojos.id WHERE dojos.id = %(id)s "
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, {"id":id})
        ninjas = []
        for row in results:
            each_ninja=cls(row)
            ninjas.append(each_ninja)
        return ninjas
    #     if results:
    #         row=results[0]
    #         one_ninja=cls(row)
    #         return one_ninja