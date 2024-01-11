from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')
def dojo():
    return 'Dojo'
@app.route('/hi/<string:name>')
def hi(name):
    print(name) 
    return "hi," + name

@app.route('/repeat/<int:dog>/<string:phrase>')
def hello_repeat (dog, phrase):
    return dog*phrase

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.