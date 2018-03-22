import os
from flask import Flask

# app configuration
app = Flask(__name__)
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

# enable cors
from flask_cors import CORS
cors = CORS(app)

# load database
from flask_peewee.db import Database
db = Database(app)

from flask_peewee.auth import Auth
from app.model.user import User
auth = Auth(app, db, user_model=User)

# set up rest api
from app.api import setup
setup(app)
