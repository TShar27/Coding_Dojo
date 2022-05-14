from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User

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

@app.route("/update_user/<int:id>")
def edit_page(id):
    user = User.get_one_user(id)
    return render_template("edit.html", user = user) # first variable can be any name as long as it matches in the jinja code

@app.route("/updateUser/<int:id>",methods = ['post']) # never see this URL 
def update_user(id):
    User.update_user(request.form,id) 
    return redirect("/")

@app.route("/destory/<int:id>")
def delete_user(id):
    User.delete_user(id)
    return redirect("/")