from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
DATABASE = "sightings_schema"

class Sasighting:
    def __init__(self,data):
        self.id= data['id']