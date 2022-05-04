from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key ="kobe shar"

@app.route('/')
def index():
    allusers = User.get_all_users()
    return render_template("index.html",users = allusers)


if __name__ == "__main__":
    app.run(debug = True,port=5001)