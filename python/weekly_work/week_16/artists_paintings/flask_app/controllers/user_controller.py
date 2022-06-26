from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.artist import Artist
from flask_app.models.paintings import Paintings



bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register',methods=['post'])
def register():
    is_valid = Artist.validate_user(request.form)

    if not is_valid:
        return redirect("/")
    new_user = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = Artist.save(new_user)
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
    user = Artist.get_by_email(data)
    print("**********************************")
    print(user.password)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect('/dashboard')


@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template("dashboard.html", artist = Artist.show_one(data), paintings = Paintings.artists_paintings(data))

@app.route("/show/<int:id>")
def tv_show(id):
    data = {
        "id": session['user_id']
    }
    
    return render_template("showOne.html", paintings = Paintings.show_one(id), artist = Artist.show_one(data))


@app.route("/edit/<int:id>")
def edit(id):
    return render_template("edit.html", paintings = Paintings.show_one(id))

@app.route("/editPainting/<int:id>",methods = ["post"])
def on_page_edit(id):
    Paintings.update(request.form,id)
    return redirect("/dashboard")


@app.route("/dashboard/add_painting") 
def new():
    return render_template("create.html")

@app.route("/add_painting", methods=["post"])
def add_painting():
    is_valid = Paintings.validate_painting(request.form)
    if not is_valid:
        return redirect("/dashboard/add_painting")
    Paintings.create(request.form)
    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete_painting(id):
    data = {
            "id": id
        }
    Paintings.deletion(data)
    return redirect("/dashboard")


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')