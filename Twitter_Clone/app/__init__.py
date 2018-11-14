from flask import Flask
from flask_mongoengine import MongoEngine
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_login import LoginManager

app=Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


from app import views, models, forms
