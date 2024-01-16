from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "hello_key"

@app.route('/')         
def index():
    if 'total_count' in session:
        session['total_count'] += 1 
    else:
        session['total_count'] = 1 
    try:
        adder = int(session.get('adder', 0))
    except ValueError:
        adder = 0
    session['added'] = session.get('added', 0) + adder

    return render_template("index.html", total_count=session['total_count'], added=session['added'])
@app.route('/destroy_session', methods= ['GET', 'POST'])
def destroy():
    
    session.pop('total_count')
    session.pop('added', None)
    session.pop('adder', None)
    return redirect("/")

@app.route('/add_two',methods= ['GET', 'POST'])
def add_two():
    session['total_count']+=1
    return redirect("/")
@app.route('/add_any',methods= ['POST'])
def add_any():
    session['adder'] = request.form['adder']
    add_value=int(request.form['adder'])-1
    session['total_count']+=add_value
    return redirect("/")

if __name__ == '__main__':
    app.run()