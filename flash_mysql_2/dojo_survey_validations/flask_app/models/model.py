from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Dojo:
    @staticmethod
    def validate_form(form):
        is_valid=True
        if len(form['name']) < 1:
            flash('Give me a real name')
            is_valid=False
        if len(form['comment'])<10:
            flash("Please give more commentary to join a dojo.")
            is_valid=False
        return is_valid 