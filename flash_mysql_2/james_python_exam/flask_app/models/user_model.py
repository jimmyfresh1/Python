from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import post_model
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATABASE = "books_schema"


class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']



    

    @classmethod
    def create (cls,form):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
"""
        return connectToMySQL (DATABASE).query_db(query,form)
    
    @classmethod
    def get_user_by_id(cls,data):
        query= """
            SELECT * FROM users WHERE id=%(user_id)s
"""
        print(query)
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        print (result[0])
        return cls(result[0])
    
    @classmethod
    def email_retrieval_test(cls,data):
        query = """
            SELECT * FROM users WHERE email=%(email)s
"""
        results=connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            flash ("Email Not In Database", 'login')
            return None
        return User(results[0])
    
    @staticmethod
    def validate(form):
        is_valid=True
        print("Trying to validate!")
        if len (form['first_name'])<2:
            print("failed first name test!")
            flash("Need more than 2 chars for first_name", "register")
            is_valid= False
        if len (form['last_name'])<2:
            print("failed second name test!")
            flash("Need more than 2 chars for last_name", "register")
            is_valid= False
        if not EMAIL_REGEX.match(form['email']): 
            print ("failed email")
            flash("Invalid email address!", "register")
            is_valid = False
        if (form['password'] != form['confirm']):
            print("Passwords do not match!")
            flash("Match your passwords", "register")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form):
        is_valid=True
        if len (form['email'])<3:
            flash("i didn't even let you in the first time", "login")
            is_valid= False
        if len (form['password'])<3:
            flash("nope. guess again", "login")
            is_valid= False
    def quickflash():
        flash("That password isn't right", "login")

    @staticmethod
    def uniqueness_test(form):
        is_valid=True
        print("I'm looking!")
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, form)
        if len(results) > 0:
            print("We found it!")
            flash("Account already exists!!", "register")
            is_valid=False
        return is_valid