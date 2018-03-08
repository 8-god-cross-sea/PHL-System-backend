from flask_peewee.rest import RestAPI
from app import app


class NoAuthentication(object):
    def authorize(self):
        return True


api = RestAPI(app, default_auth=NoAuthentication())
