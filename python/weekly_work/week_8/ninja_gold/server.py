from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key ="Timmy's a beast"

@app.route('/')
def index():
    if 'gold'  not in session:
        session['gold'] = 0
    return render_template("index.html")

@app.route('/process_money',methods =['post'])
def choice():
    session['land'] = request.form['land']
    random_number = random.randint(10,21)
    if session['land'] == 'farm':
        session['gold'] += random_number
    print(session)
    return redirect('/')


@app.route('/reset')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True,port=5001)