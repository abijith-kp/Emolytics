from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from tweepy import OAuthHandler
from flask.ext.rq import RQ

emolytics = Flask("emolytics", template_folder="server/templates/", static_folder="server/static/", static_url_path="", instance_relative_config=True)

emolytics.config.from_pyfile("config.py")

auth = OAuthHandler(emolytics.config.get('CONSUMER_KEY'), emolytics.config.get('CONSUMER_SECRET'))
auth.set_access_token(emolytics.config.get('ACCESS_TOKEN'), emolytics.config.get('ACCESS_TOKEN_SECRET'))

db = SQLAlchemy()
db.init_app(emolytics)
with emolytics.app_context():
    db.create_all()
RQ(emolytics)

from server import route
from server.models import *
