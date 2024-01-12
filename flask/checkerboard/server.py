from flask import Flask , render_template
app = Flask(__name__)    

@app.route('/')          
def index():
    return render_template("index.html")

@app.route('/checkerboard/' , defaults= {'num':8, 'num2':8})
@app.route('/checkerboard/<int:num>/', defaults = {'num2':8})
@app.route('/checkerboard/<int:num>/<int:num2>')

def checkerboard(num, num2):
    return render_template("checkerboard.html", num=num, num2=num2)

# @app.route('/<int:num>/<int:num2>')
# def playground(num, num2):
#     return render_template("checkerboard.html", num=num, num2=num2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.