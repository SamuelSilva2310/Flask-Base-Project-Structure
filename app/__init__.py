"""Initialize necessary

app, databases ...

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = "INSERT SECRET KEY HERE"
app.config['SQLALCHEMY_DATABASE_URI'] = "INSERT DATABSE URI HERE"
db = SQLAlchemy(app) #Initialize database


# Import Routes
from app import routes 

