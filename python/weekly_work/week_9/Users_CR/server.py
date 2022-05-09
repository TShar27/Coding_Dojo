from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key ="kobe shar"

@app.route("/")
def index():
    return render_template("create.html")

@app.route("/create_user", methods=["post"])
def index():
    User.create_user(request.form)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True,port=5001)