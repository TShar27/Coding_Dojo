from flask_app import app   
from flask import render_template, request, redirect, session
from flask_app.models.ninjas import Ninja
from python.weekly_work.week_11.dojos_and_ninjas.flask_app.models.ninjas import Ninja

@app.route("/")
def index():
    return render_template("index.html",users = Ninja.get_all_users())

@app.route("/read_all/create_user") # never see this URL
def new():
    return render_template("create.html")

@app.route("/create_user", methods=["post"])
def create_user():
    User.create_user(request.form)
    return redirect("/")

@app.route("/show_user/<int:id>")
def show_user(id):
    # user = User.show_one_user(id)
    return render_template("showOne.html", user = Ninja.show_one_user(id))

@app.route("/edit_user/<int:id>")
def edit(id):
    return render_template("edit.html", user = Ninja.show_one_user(id))

@app.route("/editUser/<int:id>",methods = ["post"])
def on_page_edit(id):
    User.update_user(request.form,id)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_user(id):
    User.deletion(id)
    return redirect("/")