from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user_model
class Friendship:
    def __init__( self , data ):
        self.users_full_name = data['users_full_name']
        self.friends_full_name = data['friends_full_name']

    @classmethod
    def users_and_friends(cls):
        query ="""
            SELECT
            CONCAT(users1.first_name," ", users1.last_name) AS users_full_name,
            CONCAT(friends.first_name," ", friends.last_name) AS friends_full_name
            FROM
            users AS users1
            JOIN
            friendships ON friendships.user_id = users1.id
            JOIN
            users AS friends ON friendships.friend_id = friends.id;
"""
        results = connectToMySQL('friendships_schema').query_db(query)
        formed_friendships=[]
        for friendship in results:
            formed_friendships.append(cls(friendship))
        return formed_friendships 
    
    
    @classmethod
    def new_friendship(cls, form_data):
        query ="""
        INSERT into friendships (user_id, friend_id) VALUES (%(user1id)s, %(user2id)s)
"""
        return connectToMySQL("friendships_schema").query_db(query, form_data)
