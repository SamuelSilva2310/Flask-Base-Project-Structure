"""Forms used in for input (HTML)"""
from wtforms import StringField,PasswordField,BooleanField, SubmitField,ValidationError
from wtforms.validators import DataRequired,EqualTo, Length
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm


"""
Example of a simple form used for input (html form)
"""
class ExampleForm(FlaskForm):
	name = StringField('Name', validators=[DataRequired(), Length(min=2,max=20)])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm password', validators=[DataRequired(),EqualTo('password')])

	submit = SubmitField("Submit")

