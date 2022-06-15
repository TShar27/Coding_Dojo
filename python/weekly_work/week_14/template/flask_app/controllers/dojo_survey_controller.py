from asyncio import start_unix_server
import re
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.survey import Survey

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['post'])
def create_survey():
    if Survey.required_fields(request.form):
        Survey.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def results():
    return render_template("result.html",survey = Survey.see_results())