from flask import Flask , render_template
app = Flask(__name__)    

@app.route('/')          
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return "Success"

@app.route('/play/<string:arbitrary>/<int:num_sec>')
def playground(arbitrary,num_sec):
    return render_template("play.html", arbitrary=arbitrary, num_sec=num_sec)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.