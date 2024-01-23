from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.model import Dojo


@app.route('/', )
def index():
    return render_template("index.html")
@app.route('/result', methods= ['POST'])
def result():
    if not Dojo.validate_form(request.form):
        return redirect('/')

    session['my_name']=request.form['name']
    my_name= session['my_name']
    session['dojo_location']=request.form['location']
    dojo_location=session['dojo_location']
    session['favorite_language']=request.form['language']
    favorite_language=session['favorite_language']
    session['comment_optional']=request.form['comment']
    comment_optional=session['comment_optional']

    return render_template('result.html', my_name=my_name, dojo_location=dojo_location, favorite_language=favorite_language, comment_optional=comment_optional)
