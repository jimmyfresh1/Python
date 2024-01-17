from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "hello_key"
import random
computers_numb = random.randint(1,100)
result_class=''

@app.route('/')
def index():
    global result_class
    try:
        guess_var = session.get('guess')
        if guess_var is None:
            display = "You haven't guessed yet!"
        else:
            display= int(session.get('guess'))
    except ValueError:
        display="Try a number"
    message=session.get('result')
    actual=computers_numb
    result_class=session.get('result_class')
    game_over = session.get('game_over')
    win= session.get('win')
    counter= session.get('count')
    return render_template("index.html", display=display, message=message,actual=actual, result_class=result_class, game_over=game_over, win=win, counter=counter)

@app.route('/guess',methods= ['GET', 'POST'])
def guess():
    if 'count' not in session:
        session['count']=1
    else: 
        session['count'] +=1
    session['guess'] = request.form['guess']
    try:
        user_guess=int(session['guess'])
        if user_guess == computers_numb:
            print(computers_numb)
            session['result']="Just right!"
            session['result_class']= "win"
            session['win'] = True
            return redirect('/')
        if session['count'] >5:
            session['result']= "You lose! Good day, sir!"
            session['result_class']= "lose"
            session['game_over'] = True
            return redirect('/')
        if user_guess > computers_numb:
            print(computers_numb)
            session['result']="Too high!"
            session['result_class']= "high"
            return redirect('/')
        if user_guess < computers_numb:
            print(computers_numb)
            session['result']="Too low!"
            session['result_class']= "low"
            return redirect('/')

    except ValueError:
        session['result']=user_guess="invalid"
        return redirect("/")
@app.route('/play-again')
def play_again():
    session.clear()
    return redirect('/')
# @app.route('/high')
#     return redirect("/")

# @app.route('/low')
#     return redirect("/")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

