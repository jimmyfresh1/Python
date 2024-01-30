from flask import Flask , render_template
app = Flask(__name__)    
import random

@app.route('/')          
def index():
    val=random.randint(0,50)
    print(val)
    mult=1.05
    yard=val*mult
    return render_template("index.html", yard=yard)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.