from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi all'

@app.route('/<string:first_name>/')
def newName(first_name):
    name = f"{first_name}"
    newarr = ["tony","alicia","faye"] 
    newdict = {
        "name": "Timmy Shar",
        "age": 25,
        "occupation": "figuring it out"
    }
    return render_template("index.html",first_name = first_name, newarr = newarr, length = 4,newdict = newdict)

if __name__ == "__main__":
    app.run(debug = True, port = 5001)

    