from .ResourceBase import BaseRestResource as Rest
from auth import auth
from models import User
from api import api
from flask import request


class UserResource(Rest):
    exclude = ('password', 'email',)

    def get_api_name(self):
        return 'user'

    @Rest.route('/login', ['POST'])
    def login(self):
        username = request.form['username']
        password = request.form['password']
        user = auth.authenticate(username, password)
        if user:
            auth.login_user(user)
            return self.response({'status': 'login success', 'ret_code': 0})
        else:
            return self.response({'status': 'incorrect username or password', 'ret_code': 101})

    def logout(self):
        pass

    @Rest.route('/r', ['POST'])
    def r1(self):
        return self.response({'post': 'post'})

    @Rest.route('/r', ['GET', 'PUT'])
    def r2(self):
        return self.response({'get': 'get'})


api.register(User, UserResource)