from .ResourceBase import BaseRestResource as Rest
from auth import auth
from models import User
from api import api
from flask import request, Response


class UserResource(Rest):
    exclude = ('password', 'permission')
    __user_admin_mask = int('10000', 2)

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

    @Rest.route('/logout')
    def logout(self):
        auth.logout_user()
        return Response('You are now logged out')

    @Rest.route('/')
    @Rest.permission()
    def user_detail(self):
        return self.object_detail(auth.get_logged_in_user())

    @Rest.route('/list')
    @Rest.permission(__user_admin_mask)
    def api_list(self):
        return self.object_list()


api.register(User, UserResource)
