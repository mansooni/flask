from app import db

class User(db.Document):
    id = db.IntField()
    name = db.StringField(max_length=100)
    username = db.StringField(max_length=30)
    image = db.StringField(max_length=100)
    password = db.StringField(max_length=30)
