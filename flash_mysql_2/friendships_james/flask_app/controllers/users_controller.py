from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user_model import User
from flask_app.models.friendship_model import Friendship

@app.route('/process_new_user', methods=['POST'])
def create_user():
    user_sent=request.form
    User.create(user_sent)
    return redirect('/')
