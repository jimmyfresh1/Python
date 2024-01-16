from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "hello_key"
@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():