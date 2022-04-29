from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "Timmy's a beast"

@app.route('/')
def index():
    if 'win' not in session:
        session['win'] = 0 
        session['lose'] = 0
        session['draw'] = 0
        session['rounds'] = []
        session['outcome'] = None
    return render_template("index.html")

@app.route('/choice', methods=['post'])
def choice():
    # print(request.form)
    choices = ["Rock","Paper","Scissors"]
    randoint = random.randint(0,2)
    # print(choices[randoint])
    session['MyChoice'] = request.form['choice']
    session['CompChoice'] = choices[randoint]
    if session['MyChoice'] == session['CompChoice']:
        session['draw'] += 1
        message = f"The computer chose {session['CompChoice']} and you chose {session['MyChoice']}. It was a Draw"
        color = "blue"
        session['outcome'] = "Draw"
    else:
        if session['MyChoice'] == "Rock" and session['CompChoice'] == "Paper":
            win = False
        elif session['MyChoice'] == "Rock" and session['CompChoice'] == "Scissors":
            win = True
        elif session['MyChoice'] == "Paper" and session['CompChoice'] == "Rock":
            win = True
        elif session['MyChoice'] == "Paper" and session['CompChoice'] == "Scissors":
            win = False
        elif session['MyChoice'] == "Scissors" and session['CompChoice'] == "Rock":
            win = False
        elif session['MyChoice'] == "Scissors" and session['CompChoice'] == "Paper":
            win = True
        if win :
            # session['outcome'] = {'color': 'green','match':'win'}
            session['win'] += 1
            message = f"The computer chose {session['CompChoice']} and you chose {session['MyChoice']}. You a are a beast, you won"
            color = "green"
            session['outcome'] = "Win"
        else:
            session['lose'] +=1
            message = f"The computer chose {session['CompChoice']} and you chose {session['MyChoice']}. You suck, you lost to a computer"
            color = "red"
            session['outcome'] = "Lost"
    session['rounds'].append({'message': message,'color': color})
    print(session)
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True,port=5001)