from flask import Flask, render_template # Flask is a class from the library

app = Flask(__name__)

@app.route('/') # localhost:5000 or for mac with monteray localhost:5001
def index():
    # return render_template("index.html")
    return "hello world"

@app.route('/<string:name>/<int:num>')
def newName(name,num):
    return f"hello {name} my favorite number is {num}"

# @app.route('/<string:name>/<string:last_name>')
# def lastName(name,last_name):
#     return f"hello my name is {name} {last_name}"

# @app.route('/<string:first_name>/<string:last_name>') ## passing through variables to our html file
# def bothNames(first_name,last_name):
#     name = f"{first_name} {last_name}"
#     return render_template("index.html",var_1 = first_name,var_2 = last_name)


@app.route('/<string:first_name>/')
def bothNames(first_name):
    name = f"{first_name}"
    return render_template("index.html",var_1 = first_name, num = 5)


if __name__ == "__main__":
    app.run(debug = True, port = 5001)