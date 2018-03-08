from flask_peewee.rest import RestAPI

from app import app
from auth import user_auth

api = RestAPI(app, default_auth=user_auth)
