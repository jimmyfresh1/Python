from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__( self , data ):
        self.email = data['email_addresses']
        self.created=datetime.datetime.now()

    @classmethod
    def create(cls, form_data):
        query = """
            INSERT INTO emails_table (email_addresses) 
            VALUES(%(email)s);
        """
        return connectToMySQL("email_schema").query_db(query, form_data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails_table;"
        results = connectToMySQL('email_schema').query_db(query)
        emails = []
        # Iterate over the db results and create instances of friends with cls.
        for row in results:
            emails.append(cls(row))
        return emails
    @classmethod
    def uniqueness_test(cls,form):
        is_valid=True
        query = "SELECT * FROM emails_table WHERE email_addresses = %(email)s"
        results = connectToMySQL('email_schema').query_db(query, form)
        if len(results) > 0 :
            flash("Email already exists!!")
            is_valid=False
        return is_valid
    @classmethod
    def delete_email(cls,form):
        query = "DELETE FROM emails_table WHERE email_addresses=%(delete)s;"
        connectToMySQL('email_schema').query_db(query, form)


    @staticmethod
    def validate(form):
        is_valid=True
        if not EMAIL_REGEX.match(form['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid 