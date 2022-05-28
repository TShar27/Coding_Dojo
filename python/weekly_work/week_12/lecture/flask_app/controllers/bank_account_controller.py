from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User
from flask_app.models.account import BankAccount

@app.route("/create_account/<int:id>", methods = ['post'])
def new_account(id):
    if not BankAccount.validate_account(request.form):
        return redirect(f"/add_account/{id}")
    account = BankAccount.create_account(request.form,id)
    return redirect("/")

@app.route("/add_account/<int:id>")
def add_account(id):
    oneUser = User.get_one_user(id)
    return render_template("add_account.html", user = oneUser)