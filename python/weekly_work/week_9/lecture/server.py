from flask import Flask, render_template, request, redirect, session
from user import User
app = Flask(__name__)
app.secret_key ="kobe shar"

@app.route("/")
def index():
    allusers = User.get_all_users()
    return render_template("index.html",users = allusers)

@app.route("/showUser/<int:id>")
def ShowOneUser(id):
    user = User.get_one_user(id)
    return render_template("ShowOne.html", user = user)

@app.route("/create_user", methods=["post"])
def create_user():
    User.create_user(request.form)
    print(f"this information is coming from the form in server.py line 19 {request.form}")
    return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug = True,port=5001)