from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at= data['created_at']
        self.created_at= data['updated_at']

    @classmethod 
    def create(cls, form):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"""
        return connectToMySQL("login_schema").query_db(query,form)
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s"
        result = connectToMySQL("login_schema").query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def email_retrieval_test(cls,data):
        query = """SELECT * FROM USERS WHERE email=%(email)s
"""
        results=connectToMySQL("login_schema").query_db(query,data)
        
        if not results:
            flash("Can't find that email, sir", "login")
            return None
        return User(results[0])
    @staticmethod
    def validate(form):
        is_valid=True
        if len (form['first_name'])<3:
            flash("You must be some kinda joker, need more chars", "registration")
            is_valid= False
        if len (form['last_name'])<3:
            flash("weak last name", "registration")
            is_valid= False
        if len(form['email']) <3:
            flash ("ur email must be at least 3 chars", "registration")
            is_valid=False
        if not EMAIL_REGEX.match(form['email']): 
            flash("Invalid email address!", "registration")
            is_valid = False
        if not (re.search('[0-9]',form['password'])):
            flash("Please use one number", "registration")
            is_valid = False
        if not (re.search('[A-Z]',form['password'])):
            flash("Please use one capital", "registration")
            is_valid = False
        if (form['password'] != form['password_confirmation']):
            flash("Match your passwords", "registration")
            is_valid = False

        if len(form['password']) <3:
            flash ("r u even trying", "registration")
            is_valid=False
        return is_valid
    @staticmethod
    def uniqueness_test(form):
        is_valid=True
        print("I'm looking!")
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('login_schema').query_db(query, form)
        if len(results) > 0:
            print("We found it!")
            flash("Email already exists!!", "registration")
            is_valid=False
        return is_valid

        # if len(form['email']) <3:
        #     flash ("ur email must be at least 3 chars ok?", "login")
        #     is_valid=False
        # wanted to test if it could be kept in the same method

    def validate2(form):
        is_valid=True
        if len (form['email'])<3:
            flash("i didn't even let you in the first time", "login")
            is_valid= False
        if len (form['password'])<3:
            flash("nope. guess again", "login")
            is_valid= False
            
    def quickflash():
        flash("That password isn't right", "login")





