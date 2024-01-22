from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.author_model import Author
from flask_app.models import book_model

@app.route('/')
def author():
    authors=Author.get_all()
    print(authors)
    return render_template("authors.html", authors=authors)

@app.route('/authors')
def author_redirect():
    return redirect('/')

@app.route('/process_new_author', methods=['POST'])
def create_author():
    author_sent=request.form
    Author.create(author_sent)
    return redirect('/')

@app.route('/authors/<int:author_id>')
def author_favorites(author_id):
    author_favorites_list= Author.get_author_faves(author_id)
    list_of_books=book_model.Book.get_all()
    authors=Author.get_all()
    books_author_favorited_titles =[book.title for book in author_favorites_list]
    return render_template ("author_faves.html", author_favorites_list=author_favorites_list, list_of_books=list_of_books,author_id=author_id, authors=authors,books_author_favorited_titles=books_author_favorited_titles)

@app.route('/process_author_favorite_add', methods=['POST'])
def process_author_favorite_add():
    book_id=request.form['book_id']
    author_id=request.form['author_id']
    for i in range(10):
        print(author_id)
    Author.new_author_fave(request.form)    
    return redirect(f'/authors/{author_id}')
