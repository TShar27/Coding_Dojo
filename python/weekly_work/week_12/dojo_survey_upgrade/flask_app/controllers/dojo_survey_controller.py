from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['post'])
def create_survey():
    Survey.save(request.form)
    return redirect('/result')

@app.route('/result')
def results():
    return render_template("result.html",survey = Survey.see_results())