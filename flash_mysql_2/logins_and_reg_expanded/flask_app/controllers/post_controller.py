from flask import Flask, render_template, request, redirect, session
from flask_app import app
from flask_app.models.post_model import Recipe


@app.route('/recipes/<int:recipe_id>')
def show(recipe_id):
    if 'user_id' not in session:
        return redirect('/')
    this_recipe=Recipe.get_this_recipe(recipe_id)
    return render_template('/recipes_show.html', recipe=this_recipe)

@app.route('/recipes/<int:recipe_id>/edit')
def edit(recipe_id):
    this_recipe=Recipe.get_this_recipe(recipe_id)
    if session['user_id'] != this_recipe.user_id:
        return redirect('/dashboard')
    return render_template('/recipes_edit.html', recipe=this_recipe)

@app.route('/recipes/<int:recipe_id>/edit/update', methods=['POST'])
def update_recipe(recipe_id):
    this_recipe=Recipe.get_this_recipe(recipe_id)
    if session['user_id'] != this_recipe.user_id:
        return redirect('/dashboard')
    user_id=session['user_id']
    data={
        "user_id": user_id,
        'title': request.form['title'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_30_min": request.form['under_30_min'],
        "date_cooked": request.form['date_cooked'],
        "recipe_id":recipe_id}
    if not Recipe.validate3(data):
        print("Failed to put in recipe properly")
        return redirect(f'/recipes/{recipe_id}/edit')
    print("made it through validations")
    Recipe.update_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/new')
def new_form():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('/recipes_new.html')

@app.route('/recipes/new/submit', methods=["POST"])
def new_submit():
    if 'user_id' not in session:
        return redirect('/')
    user_id=session['user_id']
    data={ 
        "user_id":user_id,
        "title":request.form['title'],
        "description":request.form['description'],
        "instructions":request.form['instructions'],
        "under_30_min":request.form.get('under_30_min'),
        "date_cooked":request.form['date_cooked']
    }
    if not Recipe.validate3(data):
        print("Failed to put in recipe properly")
        return redirect('/recipes/new')
    print("We made it through validation")
    Recipe.new_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/<int:recipe_id>/delete')
def delete(recipe_id):
    this_recipe=Recipe.get_this_recipe(recipe_id)
    if session['user_id'] != this_recipe.user_id:
        return redirect('/dashboard')
    Recipe.delete(recipe_id)
    return redirect('/dashboard')
    

