from app import db

class Blogpost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(20))
	date_posted = db.Column(db.DateTime)
	content = db.Column(db.Text)

	def __init__(self, title, subtitle, author, content, date_posted):
		self.title = title
		self.subtitle = subtitle
		self.author = author
		self.content = content
		self.date_posted = date_posted
