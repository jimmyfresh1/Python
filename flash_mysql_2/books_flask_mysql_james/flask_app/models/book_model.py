from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title=data['title']
        self.num_of_pages=data['num_of_pages']

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO books (title, num_of_pages) 
            VALUES(%(title)s, %(num_of_pages)s);
        """
        return connectToMySQL("books_schema").query_db(query, form_data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        # Iterate over the db results and create instances of friends with cls.
        for book in results:
            books.append(cls(book))
        print(books)
        return books

    @classmethod
    def get_book_faved_by(cls,book_id):
        query ="""
        SELECT CONCAT(first_name, ' ', last_name) as full_name, favorites.id, books.title, books.num_of_pages
from authors join favorites on favorites.author_id=authors.id
join books on books.id = favorites.book_id
where books.id= %(id)s"""
        results = connectToMySQL('books_schema').query_db(query, {"id":book_id})
        book_faved=[]
        for faved_by in results:
            print(faved_by)
            book_faved.append(author_model.Author(faved_by))
        print(book_faved)
        return book_faved
    
    @classmethod
    def new_book_faved_by(cls, form_data):
        query ="""
        INSERT into favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s)
"""
        return connectToMySQL("books_schema").query_db(query, form_data)
