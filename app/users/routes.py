""" Create  a Blueprint"""
from flask import Blueprint
from app.users.forms import LoginForm,RegisterForm
from flask import render_template,url_for

users=Blueprint('users', __name__)

""" Create specific routes for user only related"""


@users.route("/login", methods=['GET','POST'])
def login():
	form=LoginForm()
	return render_template("auth/login.html", form=form)


@users.route("/register", methods=['GET','POST'])
def register():
	form=RegisterForm()
	return render_template("auth/login.html", form=form)