from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.full_name=data['full_name']

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO authors (first_name, last_name) 
            VALUES(%(first_name)s, %(last_name)s);
        """
        return connectToMySQL("books_schema").query_db(query, form_data)

    @classmethod
    def get_all(cls):
        query = "SELECT id, CONCAT(first_name, ' ', last_name) AS full_name FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        # Iterate over the db results and create instances of friends with cls.
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def get_author_faves(cls,author_id):
        query ="""
        SELECT books.title, books.num_of_pages, favorites.id
from authors join favorites on favorites.author_id=authors.id
join books on books.id = favorites.book_id
where authors.id= %(id)s"""
        results = connectToMySQL('books_schema').query_db(query, {"id":author_id})
        author_faves=[]
        for author_fave in results:
            author_faves.append(book_model.Book(author_fave))
        return author_faves

    @classmethod
    def new_author_fave(cls, form_data):
        query ="""
        INSERT into favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s)
"""
        return connectToMySQL("books_schema").query_db(query, form_data)
