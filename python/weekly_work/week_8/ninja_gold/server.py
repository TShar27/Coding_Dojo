from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key ="Timmy's a beast"

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/reset')
def clear():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True,port=5001)