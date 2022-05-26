from flask_app import app   
from flask import render_template, request, redirect, session
from flask_app.models.ninjas import Ninja

@app.route("/")
def index():
    return render_template("index.html",ninjas = Ninja.get_all_ninjas())

@app.route("/read_all/create_ninja")
def new():
    return render_template("create.html")

@app.route("/create_ninja", methods=["post"])
def create_user():
    Ninja.create_ninja(request.form)
    return redirect("/")

@app.route("/show_ninja/<int:id>")
def show_ninja(id):
    # user = User.show_one_user(id)
    return render_template("showOne.html", ninja = Ninja.show_one_ninja(id))

@app.route("/edit_ninja/<int:id>")
def edit(id):
    return render_template("edit.html", ninja = Ninja.show_one_ninja(id))

@app.route("/editNinja/<int:id>",methods = ["post"])
def on_page_edit(id):
    Ninja.update_ninjas(request.form,id)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_ninja(id):
    Ninja.deletion(id)
    return redirect("/")

@app.route("/show_dojo/<int:id>")
def show_account(id):
    return render_template("showNinjaDojo.html", ninja = Ninja.get_all_ninjas_with_dojo(id))