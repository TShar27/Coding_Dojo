from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.tv_shows import TvShow 


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register',methods=['post'])
def register():
    is_valid = User.validate_user(request.form)

    if not is_valid:
        return redirect("/")
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = User.save(new_user)
    if not id:
        flash("Email already taken.","register")
        return redirect('/')
    session['user_id'] = id
    return redirect('/')


@app.route("/login",methods=['post'])
def login():
    data = {
        "email": request.form['email']
    }
    user = User.get_by_email(data)
    print("**********************************")
    print(user.password)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect('/')


@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template("dashboard.html", user = User.show_one_user(data), tv_show = TvShow.user_tv_shows(data))

@app.route("/show/<int:id>")
def tv_show(id):
    is_valid = TvShow.validate_show(request.form)
    
    data = {
        "id": session['user_id']
    }
    
    return render_template("showOne.html", tv_show = TvShow.show_one_tv_show(id), user = User.show_one_user(data))


@app.route("/edit/<int:id>")
def edit(id):
    return render_template("edit.html", tv_show = TvShow.show_one_tv_show(id))

@app.route("/editTvShow/<int:id>",methods = ["post"])
def on_page_edit(id):
    TvShow.update_tv_show(request.form,id)
    return redirect("/dashboard")


@app.route("/dashboard/add_show") 
def new():
    return render_template("create.html")

@app.route("/add_show", methods=["post"])
def add_tv_show():
    TvShow.create_tv_show(request.form)
    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete_tv_show(id):
    data = {
            "id": id
        }
    TvShow.deletion(data)
    return redirect("/dashboard")


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')