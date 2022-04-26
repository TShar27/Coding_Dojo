# get request - requesting data from the server
# post request - Can take in data, store and update it. Sending info to a server to get something back 

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "I love coding"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/buy', methods=["post"])
def buy():
    print(request.form)
    data = { # accesing dictionary values 
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'meatballs': request.form['meatballs'],
        'student_id': request.form['id']
    }
    return render_template("buy.html", data = data)

   # you can do the same thing with session ^

if __name__ == "__main__":
    app.run(debug = True,port = 5001)