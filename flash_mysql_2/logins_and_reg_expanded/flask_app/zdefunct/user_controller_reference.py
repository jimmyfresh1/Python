from flask import Flask, render_template, request, redirect, session
from flask_app import app
from logins_and_reg_expanded.flask_app.defunct.user_model_reference import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def registration():
    if not User.uniqueness_test(request.form):
        return redirect('/')
    hash = bcrypt.generate_password_hash(request.form['password'])
    if not User.validate(request.form):
        return redirect('/')
    new_user={
        'first_name': request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':hash
    }
    user_id=User.create(new_user)
    session['user_id']=user_id
    return redirect('/dashboard')

@app.route('/login', methods= ['POST'])
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