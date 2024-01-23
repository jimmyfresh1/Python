from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.model import Email

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/success',methods= ['POST'])
def succeed():
    
    if not Email.validate(request.form):
        return redirect('/')
    Email.create(request.form)
    emails = Email.get_all()
    newmail=request.form['email']
    return render_template('success.html', emails=emails, newmail=newmail)
