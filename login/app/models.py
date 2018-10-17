from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	__tablename__="User"
	__table_args__ = {'mysql_collate':'utf8_general_ci'}
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password
