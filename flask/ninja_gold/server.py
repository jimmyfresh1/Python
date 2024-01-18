from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)  
app.secret_key = "hello_key"
gold_dict = { "farm": (5 , 12),  "cave": (1, 20) ,"house": (7,7),  "casino": (-50, 50)}

@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity' not in session:
        session['activity']=''
    if 'activity_history' not in session:
        session['activity_history']=[]
    if session['count']>30:
        session['activity_history'] =["YOU LOSE CHUMP "]
        session['play_again'] = 'Play Again?'
    gold = session.get('gold', 0) 
    activity = session.get ('activity', '')
    earnings = session.get('earnings',0)
    activity_history=session.get('activity_history', '')
    if session['gold']>=500:
        session['activity_history'] =["YOU'RE A WINNER!"]
        session['play_again'] = 'Play Again?'
    return render_template('index.html', gold=gold, activity=activity, activity_history=activity_history)

@app.route('/process_money', methods=['POST'])
def process_money():
    timestamp = datetime.now()
    session['locus']=request.form['locus']
    locus_visited=session['locus']
    min_gold, max_gold = gold_dict[locus_visited]
    earnings = random.randint(min_gold, max_gold)
    session['activity']=""
    if 'activity_history' not in session:
        session['activity_history']=[]
    if locus_visited =="casino":
        if earnings < 0:
            session['activity'] = f"Oh no! You lost {earnings} gold! {timestamp}"
        if earnings == 0: 
            session['activity'] = f"Could be worse! Made none and lost none! {timestamp}"
        if earnings >0:
            session['activity'] =f"Right on! You made {earnings} gold! {timestamp}"
    else:
        session['activity'] = f"You earned {earnings} gold in that {locus_visited}! {timestamp}"
    session['activity_history'].insert(0,(session['activity']))
    session['gold'] += earnings
    session['count'] +=1
    return redirect ('/')


@app.route('/reset', methods=['GET'])
def reset ():
    session.clear()
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.