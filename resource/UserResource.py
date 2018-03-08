from flask_peewee.rest import RestResource

from auth import auth
from models import User
from api import api
from flask import request


class UserResource(RestResource):
    exclude = ('password', 'email',)

    def get_api_name(self):
        return 'user'

    def get_urls(self):
        return [
            ('/login', self.login),
            ('/logout', self.logout)
        ]

    def login(self):
        username = request.form['username']
        password = request.form['password']
        user = auth.authenticate(username, password)
        if user:
            auth.login_user(user)
            return self.response({'status': 'login success', 'ret_code': 0})
        else:
            return self.response({'status': 'xxx', 'ret_code': 101})

    def logout(self):
        pass


api.register(User, UserResource)
