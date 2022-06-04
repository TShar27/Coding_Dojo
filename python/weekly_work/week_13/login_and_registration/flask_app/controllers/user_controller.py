from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", method = ['post'])
def register():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'confirm':request.form['confirm']
    }
    User.save(data)
