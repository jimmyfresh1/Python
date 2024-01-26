from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
from datetime import datetime

class Recipe:
    def __init__(self,data):
        self.id=data.get('id')
        self.user_id=data.get('user_id')
        self.title=data.get('title')
        self.description=data.get('description')
        self.instructions=data.get('instructions')
        self.date_cooked=data.get('date_cooked')
        self.under_30_min=data.get('under_30_min')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

    @classmethod
    def new_recipe(cls, data):
        query = """
            INSERT INTO posts (user_id, title, description, instructions, date_cooked, under_30_min)
            VALUES (%(user_id)s, %(title)s, %(description)s,%(instructions)s,%(date_cooked)s,%(under_30_min)s)
            """
        results = connectToMySQL("recipes_schema").query_db(query,data)

    @classmethod
    def update_recipe (cls,data):
        query = """
            UPDATE posts
            SET user_id= %(user_id)s,  title=%(title)s, description=%(description)s, date_cooked=%(date_cooked)s, instructions= %(instructions)s, under_30_min= %(under_30_min)s
            WHERE id = %(recipe_id)s;
"""
        return connectToMySQL("recipes_schema").query_db(query,data)
    

    @classmethod 
    def get_all_recipes(cls):
        query = """
SELECT * 
from posts 
JOIN users ON posts.user_id=users.id 
    """
        results= connectToMySQL("recipes_schema").query_db(query)
        if not results:
            print("Either no results, or wrong query")
            return []
        all_recipes= []
        for row in results:
            recipe = cls(row)
            creator_data = {
                'id':row['users.id'],
                'first_name':row['first_name']}
            recipe.creator=user_model.User(creator_data)
            print(recipe.creator.last_name)
            all_recipes.append(recipe)

        return all_recipes

    @classmethod
    def get_this_recipe(cls, recipe_id):
        id_query = {
        'recipe_id': recipe_id
    }
        query= """
            SELECT * 
            FROM posts 
            JOIN users ON users.id=posts.user_id
            WHERE posts.id=%(recipe_id)s
"""
        result = connectToMySQL("recipes_schema").query_db(query, id_query)
        row = result[0]
        recipe = cls(row)
        creator_data = {
            'id':row['users.id'],
            'first_name':row['first_name']}
        recipe.creator=user_model.User(creator_data)
        return recipe 
    
    @staticmethod
    def validate3(data):
        is_valid=True
        print("Can we validate this recipe?")
        print("Under 30 min value:", data['under_30_min'])
        if len(data['title']) < 3:
            flash("No cooking for lazy people! Needs title!", "recipes")
            is_valid=False 
        if len(data['description'])  <3:
            flash("No cooking for lazy people! Needs description!", "recipes")
            is_valid=False 
        if len(data['instructions']) <3:
            flash("No cooking for lazy people!  Needs instructions!", "recipes")
            is_valid=False 
        if data['under_30_min'] is None:
            flash("Well? Is it quick and easy or not?", "recipes")
            is_valid=False 
        try:
            date=datetime.strptime(data['date_cooked'], '%Y-%m-%d')
        except ValueError:
            flash("Date format wrong", "recipes")
            is_valid=False
            return is_valid
        current_date=datetime.today()
        if date>current_date:
            print("Time travel")
            flash("Some kinda time traveller are ya?", "recipes")
            is_valid=False
        return is_valid 
    @classmethod
    def delete(cls, delete_id):
        query = "DELETE FROM posts WHERE id = %(id)s"
        query_delete_id={"id":delete_id}
        return connectToMySQL("recipes_schema").query_db(query,query_delete_id)


