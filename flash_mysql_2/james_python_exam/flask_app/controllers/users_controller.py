from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def registration():
    print("create?")
    if not User.uniqueness_test(request.form):
        print("Failed uniqueness!!")
        return redirect('/')
    if not User.validate(request.form):
        print("Failed! validation!")
        return redirect('/')
    print("Passed validation!")
    hash = bcrypt.generate_password_hash(request.form['password'])
    new_user={
        'first_name': request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':hash
    }
    user_id=User.create(new_user)
    session['user_id']=user_id
    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    data={'email':request.form['email']}
    found_user=User.email_retrieval_test(data)
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
        print("The id was in session!")
        user_id=session['user_id']
        print(user_id)
        print(session['user_id'])
        data1 = {
            'user_id':user_id
        }
        print(data1)
        current_user= User.get_user_by_id(data1)
        return render_template("dashboard.html", current_user=current_user)
    else:
        print("the id WAS NOT IN SESSION")
        return redirect('/')
    
    
@app.route ('/logout')
def destroy_session():
    session.clear()
    return redirect('/')
