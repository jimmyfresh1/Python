from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "hello_key"
import random
computers_numb = random.randint(1,100)

@app.route('/')
def index():
    try:
        display= int(session.get('guess'))
    except ValueError:
        display="Try a number"
    message=session.get('result')
    actual=computers_numb
    return render_template("index.html", display=display, message=message,actual=actual)

@app.route('/guess',methods= ['GET', 'POST'])
def guess():
    if 'count' not in session:
        session['count']=1
    else: 
        session['count'] +=1
    session['guess'] = request.form['guess']
    try:
        user_guess=int(session['guess'])
        if session['count'] >=5:
            session['result']= "You lose! Good day, sir!"
            result_class= "lose"
            session['game_over'] = True
            return redirect(url_for('/index', result_class=result_class))
        if user_guess > computers_numb:
            print(computers_numb)
            session['result']="Too high!"
            return redirect('/')
        if user_guess < computers_numb:
            print(computers_numb)
            session['result']="Too low!"
            return redirect('/')
        if user_guess == computers_numb:
            print(computers_numb)
            session['result']="Just right!"
            result_class="win"
            return redirect(url_for('/index', result_class=result_class))
    except ValueError:
        session['result']=user_guess="invalid"
        return redirect("/")
@app.route('/play_again')
def play_again():
    session.clear()

# @app.route('/high')
#     return redirect("/")

# @app.route('/low')
#     return redirect("/")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

