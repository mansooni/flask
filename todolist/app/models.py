from app import db

class TodoList(db.Model):
	__tablename__ = "todo"
	__table_args__ = {'mysql_collate': 'utf8_general_ci'}
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.Text)
	chk = db.Column(db.Boolean)

	def __init__(self, content, chk):
		self.content = content
		self.chk = chk

