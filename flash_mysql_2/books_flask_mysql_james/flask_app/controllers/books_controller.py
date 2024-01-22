from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.book_model import Book
from flask_app.models import author_model

@app.route('/books')
def books():
    books=Book.get_all()
    return render_template("books.html", books=books)

@app.route('/process_new_book', methods=['POST'])
def create_book():
    book_sent=request.form
    Book.create(book_sent)
    return redirect('/books')

@app.route('/books/<int:book_id>')
def faved_by(book_id):
    favorited_by_list = Book.get_book_faved_by(book_id)
    authors=author_model.Author.get_all()
    favorited_by_names = [author.full_name for author in favorited_by_list]
    books = Book.get_all()
    return render_template ("book_faved.html", favorited_by_list=favorited_by_list, books=books, book_id=book_id,authors=authors,favorited_by_names =favorited_by_names)

@app.route('/process_book_faved_by', methods=['POST'])
def process_book_faved_by():
    author_id=request.form['author_id']
    book_id=request.form['book_id']
    Book.new_book_faved_by(request.form)
    return redirect(f'/books/{book_id}')

