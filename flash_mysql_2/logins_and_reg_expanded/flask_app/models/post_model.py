from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Recipe:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.title=data['title']
        self.description=data['description']
        self.instructions=data['instructions']
        self.date_cooked=data['date_cooked']
        self.under_30_min=data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def new_recipe(data):
    query = """
        INSERT INTO posts (user_id, title, description, instructions, date_cooked, under_30_min)
        VALUES (%(user_id)s, %(title)s, %(description)s,%(instructions)s,%(date_cooked)s,%(under_30_min)s)
        """
    results = connectToMySQL("recipes_schema").query_db(query,data)
@classmethod
def get_this_recipe()
@staticmethod
def validate3(data):
    is_valid=True
    print("Can we validate this recipe?")
    if not data['user_id']:
        print("Not even logged in,bro")
        flash ("Log in! I won't ask you twice!", "recipes")
    if len(data['title']) < 3 or  len(data['description'])  or len(data['instructions']) <3:
        print("No cooking for lazy people!")
        flash("No cooking for lazy people!", "recipes")
    return is_valid

    
    
