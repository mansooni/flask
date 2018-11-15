from app import db, login_manager
from flask_login import UserMixin


class User(UserMixin, db.Document):
    name = db.StringField(max_length=100)
    username = db.StringField(max_length=30)
    image = db.StringField(max_length=100)
    password = db.StringField(max_length=1000)
    join_date = db.DateTimeField()


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

class Tweet(db.Document):
    user_id = db.ReferenceField(User)
    text = db.StringField(max_length=140)
    date_created = db.DateTimeField()
