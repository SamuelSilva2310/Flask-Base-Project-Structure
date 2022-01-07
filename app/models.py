"""Databse Models (Tables)"""
from app import db
from datetime import datetime

"""Example of a simple Model (DB Table)"""
class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(30),unique=True,nullable=False)

	def __repr__(self):
		return f"User '{self.id}','{self.username}'"