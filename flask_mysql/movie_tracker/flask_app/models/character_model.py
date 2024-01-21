from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.movie_model import Movie



class Character:
    def __init__(self, data):
        self.id = data["id"] 
        self.name = data["name"] 
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.movie_id = data["movie_id"]



    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO characters (name, movie_id)
            VALUES(%(name)s,%(movie_id)s);
        """
        return connectToMySQL("allmovies_db").query_db(query, form_data)
    

    @classmethod
    def get_all_with_movies(cls):

        query = """
            SELECT * FROM characters JOIN movies ON characters.movie_id = movies.id;
        """

        results = connectToMySQL("allmovies_db").query_db(query)


        characters = []

        for row in results:
            new_character = cls(row)

            movie_data = {
                **row,
                "id" : row["movies.id"],
                "created_at" : row["movies.created_at"],
                "updated_at" : row["movies.updated_at"]
            }

            new_movie = Movie(movie_data)

            new_character.movie = new_movie
            
            characters.append(new_character)
        return characters






# my_dict ={
#     "1" : "a",
#     "2" : "b",
#     "3" : "c"
# }



# new_dict = {
#     **my_dict,
#     "4" : "d",
#     "5" : "e"
# }


# print(new_dict)