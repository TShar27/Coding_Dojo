from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.restaurants import Restaurants
from flask_app.models.reviews import Reviews

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
    return redirect('/dashboard')


@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    return render_template("dashboard.html", user = User.show_one(data), restaurants = Restaurants.restaurants_to_be_reviewed(data), reviews = Reviews.reviewed_restauarnts (data))

@app.route("/restaurant/<int:id>")
def restaurant_review(id):
    data = {
        "id": session['user_id']
    }
    return render_template("showOne.html", restaurants = Restaurants.show_one(id), reviews = Reviews.single_restaurant_reviews(data)) # my question is how can I call on a different model which has a different query in the same function? 
    # my problem is that I have no way of calling another parameter, restaurants_id, within the function


@app.route("/edit/<int:id>")
def edit(id):
    return render_template("edit.html", paintings = Restaurants.show_one(id))

@app.route("/editPainting/<int:id>",methods = ["post"])
def on_page_edit(id):
    Restaurants.update(request.form,id)
    return redirect("/dashboard")


@app.route("/dashboard/add_painting") 
def new():
    return render_template("create.html")

@app.route("/add_painting", methods=["post"])
def add_painting():
    is_valid = Restaurants.validate_painting(request.form)
    if not is_valid:
        return redirect("/dashboard/add_painting")
    Restaurants.create(request.form)
    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete_painting(id):
    data = {
            "id": id
        }
    Restaurants.deletion(data)
    return redirect("/dashboard")


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')