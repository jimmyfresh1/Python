from flask import Flask , render_template
app = Flask(__name__)    




@app.route('/')          
def index():
    return render_template("index.html")

@app.route('/bootstrap_dictionary/users')
def boot_dict():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("bootstrap_dictionary.html", users=users)

# @app.route('/<int:num>/<int:num2>')
# def playground(num, num2):
#     return render_template("checkerboard.html", num=num, num2=num2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.