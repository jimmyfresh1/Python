from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.model import Email

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/success')
def succeed():
    Email.validate(request.form)