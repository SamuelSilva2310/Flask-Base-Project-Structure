"""Forms used in for input (HTML)"""
from wtforms import StringField,PasswordField,BooleanField, SubmitField,ValidationError
from wtforms.validators import DataRequired,EqualTo, Length,Email
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm



"""
form used for Login (html form)
"""
class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")


"""
form used for Registrattion (html form)
"""
class RegisterForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])
	email = StringField('Email', validators=[DataRequired(),Email()])

	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])

	remember = BooleanField("Remember Me")
	submit = SubmitField("Sign Up")

