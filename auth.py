from flask_peewee.auth import Auth
from flask_peewee.rest import UserAuthentication, AdminAuthentication

from app import app, db
from models import User

auth = Auth(app, db, user_model=User)

user_auth = UserAuthentication(auth)
admin_auth = AdminAuthentication(auth)
