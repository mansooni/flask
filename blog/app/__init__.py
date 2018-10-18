from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db = SQLAlchemy(app)


app.config.from_object('config')
app.secret_key='thisisblogexmaple'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app import views,models
