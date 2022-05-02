from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key ="Timmy's a beast"

@app.route('/')
def index():
    if 'gold'  not in session:
        session['gold'] = 0
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money',methods =['post'])
def choice():
    session['land'] = request.form['land']
    if session['land'] == 'farm':
        gold_amount = random.randint(10,21)
        session['gold'] += gold_amount
        message = f" Ninja earned {gold_amount} gold from the farm"
        color = "green"
    if session['land'] == 'cave':
        gold_amount = random.randint(5,11)
        session['gold'] += gold_amount
        message = f" Ninja earned {gold_amount} gold from the cave"
        color = "brown"
    if session['land'] == 'house':
        gold_amount = random.randint(2,6)
        session['gold'] += gold_amount
        message = f" Ninja earned {gold_amount} gold from the house"
        color = "orange"
    if session['land'] == 'casino':
        gold_amount = random.randint(-50,51)
        session['gold'] += gold_amount
        message = f" Ninja earned {gold_amount} gold from the casino"
        color = "purple"
    session['activities'].append({'message':message, 'color': color})
    print(session)
    return redirect('/')


@app.route('/reset')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True,port=5001)