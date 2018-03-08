from flask_peewee.rest import RestAPI, UserAuthentication, AdminAuthentication

from app import app
from auth import auth


user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)


api = RestAPI(app, default_auth=user_auth)
