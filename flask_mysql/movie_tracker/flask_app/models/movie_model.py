from flask_app.config.mysqlconnection import connectToMySQL

class Movie:
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.release_year = data["release_year"]
        self.rating = data["rating"]
        self.length = data["length"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM movies
        """
        results = connectToMySQL("allmovies_db").query_db(query)
        print(results)
        movies = []
        for row in results:
            new_movie = cls(row)
            movies.append(new_movie)
        return movies
    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO movies (title, release_year, rating, length, description) 
            VALUES(%(title)s, %(release_year)s, %(rating)s, %(length)s, %(description)s);
        """
        return connectToMySQL("allmovies_db").query_db(query, form_data)
    @classmethod
    def delete(cls, id):
        data = {
            "id":id
        }
        query = """
            DELETE FROM movies WHERE id = %(id)s
        """
        connectToMySQL("allmovies_db").query_db(query, data)
    @classmethod
    def get_one(cls, id):
        data = {
            "id":id
        }
        query = """
            SELECT * FROM movies WHERE id = %(id)s
        """
        results = connectToMySQL("allmovies_db").query_db(query, data)
        if results:
            row = results[0]
            new_movie = cls(row)
            return new_movie
        
    @classmethod
    def update(cls, data):
        query = """
            UPDATE movies SET
            title = %(title)s,
            release_year = %(release_year)s,
            rating = %(rating)s,
            length = %(length)s,
            description = %(description)s
            WHERE id = %(id)s
        """
        connectToMySQL("allmovies_db").query_db(query, data)