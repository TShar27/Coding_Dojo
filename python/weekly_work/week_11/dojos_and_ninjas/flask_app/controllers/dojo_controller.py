from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninjas import Ninja

@app.route("/create_dojo/<int:id>", methods = ['post'])
def new_account(id):
    account = Dojo.create_dojo(request.form,id)
    return redirect("/")

# @app.route("/add_account/<int:id>")
# def add_account(id):
#     oneUser = User.get_one_user(id)
#     return render_template("add_account.html", user = oneUser)