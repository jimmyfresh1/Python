from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas')
def new_ninja_form():
    dojos=Dojo.get_all()
    return render_template ("ninjas.html", dojos=dojos)


@app.route('/create_ninja', methods= ['POST'])
def create_ninja_process():
    sent_form=request.form
    for _ in range(10):
        print(sent_form)
    Ninja.create(sent_form)
    id=request.form['dojo_id']
    return redirect(f'/show/{id}')

@app.route("/show/<int:id>")    
def show_user(id):
    ninjas=Ninja.get_all_in_dojo(id)
    return render_template("show.html", ninjas=ninjas)