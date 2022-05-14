from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key ="kobe shar"

@app.route("/")
def index():
    return render_template("index.html",users = User.get_all_users())

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
    return render_template("showOne.html", user = User.show_one_user(id))

@app.route("/edit_user/<int:id>")
def edit(id):
    return render_template("edit.html", user = User.show_one_user(id))

@app.route("/editUser/<int:id>",methods = ["post"])
def on_page_edit(id):
    User.update_user(request.form,id)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_user(id):
    User.deletion(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True,port=5001)