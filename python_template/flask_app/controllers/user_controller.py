from flask import Flask, render_template, request, redirect, session
from flask_app import app
@app.route('/')
def index():
    return render_template('index.html')
# @app.route('/dashboard')
# def dashboard():

    # if 'user_id' in session:
    #     user_id=session['user_id']
    #     data = {
    #         'user_id':user_id
    #     }
    #     #method call that gets data by that one user id, and then saves that value to a variable
    #     # current_user = User.get_user_by_id(data)
    #     return render_template("dashboard.html",current_user = current_user)
    # else: 
    #     return redirect('/')
    
@app.route ('/logout')
def destroy_session():
    session.clear()
    return redirect('/')