from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.user import Model

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def new_character():
    return render_template("create.html")
    
@app.route("/process_character_create", methods=["POST"] )
def create_user():
    id= Model.create(request.form)
    return redirect(f'/show/{id}')

@app.route("/read_all")    
def read_all():
    users = Model.get_all()
    return render_template("read_all.html", users=users)

@app.route("/show/<int:id>")    
def show_user(id):
    user=Model.get_one(id)
    return render_template("show.html", user=user)

@app.route("/edit/<int:id>")
def edit_user(id):
    user = Model.get_one(id)
    return render_template("edit.html", user=user)

@app.route("/process_character_edit", methods=["POST"] )
def edit_user_process():
    Model.update(request.form)
    user_id=request.form['id']
    return redirect(f'/show/{user_id}')

@app.route("/delete/<int:id>")
def delete(id):
    Model.delete(id)
    return redirect('/read_all')

if __name__ == "__main__":
    app.run(debug=True)

