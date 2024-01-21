from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.models.dojo_model import Dojo

@app.route('/')
def dojo():
    dojos=Dojo.get_all()
    return render_template("dojos.html", dojos=dojos)

@app.route('/dojos')
def dojo_redirect():
    return redirect('/')

@app.route('/create_dojo', methods= ["POST"])
def create_dojo():
    dojo_sent_form=request.form
    for _ in range(10):
        print(dojo_sent_form)
    Dojo.create(dojo_sent_form)
    return redirect('/')

# @app.route("/show/<int:id>")    
# def show_dojo_ninjas(id):
#     user=Dojo.get_all_in_dojo(id)
#     return render_template("show.html", ninja=ninja)

