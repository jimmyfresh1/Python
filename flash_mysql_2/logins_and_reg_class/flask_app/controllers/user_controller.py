from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/registration', methods=['POST'])
def registration():
    if not User.uniqueness_test(request.form):
        return redirect('/')
    print("Here I am", request.form)
    temp_dict=request.form
    print(request.form['password'])
    hash = bcrypt.generate_password_hash(request.form['password'])
    print(hash)
    if not User.validate(temp_dict):
        return redirect('/')
    new_user={
        'first_name': request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':hash
    }
    #inserting into database returns the id of the newly created user
    user_id=User.create(new_user)
    session['user_id']=user_id
    return redirect('/dashboard')

@app.route('/user/login', methods= ['POST'])
def login():
    # temp_dict2=request.form
    # if not User.validate2(temp_dict2):
    #     return redirect('/')

    data= {
        'email': request.form['email']
    }
    found_user = User.email_retrieval_test(data)
    if not bcrypt.check_password_hash(found_user.password, request.form['password']):
        User.quickflash()
        return redirect('/')
    if found_user:
        session['user_id'] = found_user.id
        return redirect('/dashboard')
    return redirect('/')
    
@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id=session['user_id']
        data = {
            'user_id':user_id
        }
        current_user = User.get_user_by_id(data)
        return render_template("dashboard.html", current_user=current_user)
    else: 
        return redirect('/')
    
@app.route ('/logout')
def destroy_session():
    session.clear()
    return redirect('/')