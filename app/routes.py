"""Used for routes"""
from flask import render_template, url_for,redirect,flash

from app.forms import ExampleForm
from app.models import User

# Import the app (Flask Instance in __init__.py)
from app import app

@app.route('/')
def index():
	return "Hello"


@app.route('/2')
def index2():
	form = ExampleForm()
	return render_template("pages/index.html",form=form)