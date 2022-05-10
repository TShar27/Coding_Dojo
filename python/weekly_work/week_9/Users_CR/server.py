from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key ="kobe shar"

@app.route("/")
def index():
    return redirect("/read_all")

@app.route("/read_all/create_user")
def new():
    return render_template("create.html")

@app.route("/create_user", methods=["post"])
def create_user():
    User.create_user(request.form)
    return redirect("/read_all")

@app.route("/read_all")
def all_users():
    return render_template("read_all.html",users = User.get_all_users())


if __name__ == "__main__":
    app.run(debug = True,port=5001)