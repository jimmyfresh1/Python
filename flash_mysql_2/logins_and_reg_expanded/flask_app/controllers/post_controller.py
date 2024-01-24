from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.post_model import Recipe


@app.route('/recipes/<int:recipe.id>')
def show():
    this_recipe=Recipe.get_this_recipe()
    return render_template('/recipes_show.html')


@app.route('/recipes/new')
def new_form():
    
    return render_template('/recipes_new.html')

@app.route('/recipes/new/submit')
def new_submit():
    user_id=session['user_id']
    data={ 
        "user_id":['user_id'],
        "title":request.form['title'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "under_30_min":request.form['under_30_min'],
        "date_cooked":request.form['date_cooked']
    }
    if not Recipe.validate3(data):
        print("Failed to put in recipe properly")
        return('/recipes/new')

    return redirect('/dashboard')
    
@app.route('/recipes/edit')
def edit():
    
    return render_template('/recipes_edit.html')

@app.route('/recipes/<int:recipe.id>/edit/submit')
def edit_submit():
    user_id=session['user_id']
    data={
        "user_id": user_id,
        'title': request.form['title'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_30_min": request.form['under_30_min'],
        "date_cooked": request.form['date_cooked']}
    if not Recipe.validate3(data):
        print("Failed to put in recipe properly")
        return('/recipes/new')
    Recipe.new_recipe(data)

    return redirect('/dashboard')