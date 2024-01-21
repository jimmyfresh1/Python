from flask import Flask, render_template, request, redirect
from models import Model
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create")
def new_character():
    return render_template("create.html")
    

@app.route("/process_character_create", methods=["POST"] )
def create_user():
    Model.create(request.form)
    return redirect('/read_all')

@app.route("/read_all")    
def read_all():
    users = Model.get_all()
    return render_template("read_all.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)

