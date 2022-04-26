# get request - requesting data from the server
# post request - Can take in data, store and update it. Sending info to a server to get something back 

import re
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "I love coding"

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/buy', methods=["post"])
# def buy():
#     print(request.form)
#     data = { # accesing dictionary values 
#         'first_name': request.form['fname'],
#         'last_name': request.form['lname'],
#         'meatballs': request.form['meatballs'],
#         'student_id': request.form['id']
#     }
#     return render_template("buy.html", data = data)

   # you can do the same thing with session (below)

@app.route('/buy',methods=['post'])
def buy():
    print(request.form)
    total = int(request.form['count']) * 2
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['food'] = request.form['food']
    session['student_id'] = request.form['id']
    session['count'] = request.form['count']
    session['total'] = total
    return redirect('/buy_stuff')

@app.route('/buy_stuff')
def buy_stuff():
    return render_template('buy.html')


@app.route('/buy_samosa',methods=['post'])
def samosas():
    print(request.form)
    total = int(request.form['count']) * 4
    session['food'] = request.form['food']
    session['count'] = request.form['count']
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['student_id'] = request.form['id']
    session['total'] = total
    return redirect('/samosa')

@app.route('/samosa')
def sam():
    return render_template('buy.html')

@app.route('/clear_session')
def clear():
    # session.clear()
    session.pop('student_id')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True,port = 5001)