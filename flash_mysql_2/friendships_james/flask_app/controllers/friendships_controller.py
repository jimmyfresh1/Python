from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user_model import User
from flask_app.models.friendship_model import Friendship

@app.route('/')
def friendslist():
    users_friends=Friendship.users_and_friends()
    all_users=User.get_all()
    return render_template("friendships.html", users_friends=users_friends, all_users=all_users)

@app.route('/process_new_friendship',methods= ["POST"])
def newfriend():
    friend_form=request.form
    Friendship.new_friendship(friend_form)
    return redirect('/')
