from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.movie_model import Movie
from flask_app.models.character_model import Character

@app.route('/')
def dashboard():
    return render_template("dashboard.html", movies_list=Movie.get_all())
@app.route('/characters')
def characters():
    return render_template("all_characters.html", characters =Character.get_all_with_movies())
@app.route('/new_character')
def new_character():
    return render_template("new_character.html",movies=Movie.get_all())
@app.route('/create_character', methods=["POST"])
def create_character():
    Character.create(request.form)
    return redirect('/characters')
@app.route('/new_movie')
def new_movie():
    return render_template("new_movie.html")
@app.route('/create_movie', methods=["POST"])
def create_movie():
    Movie.create(request.form)
    return redirect('/')
@app.route('/update/<int:id>')
def update_movie(id):
    return render_template("update_movie.html", movie = Movie.get_one(id))
@app.route('/save', methods=["POST"])
def save_movie():
    Movie.update(request.form)
    return redirect("/")
@app.route('/delete/<int:id>')
def delete(id):
    Movie.delete(id)
    return redirect('/')