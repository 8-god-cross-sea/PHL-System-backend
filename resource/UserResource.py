from .ResourceBase import BaseRestResource as Rest
from .ResponseManager import make_status_response
from .APIRestResource import APIRestResource
from .AccessControl import AccessControl as Access
from auth import auth
from models import User
from api import api
from flask import request
import json
from flask_peewee.utils import make_password


class UserResource(APIRestResource):
    exclude = ('password', 'permission')

    def __init__(self, rest_api, model, authentication, allowed_methods=None):
        super().__init__(rest_api, model, authentication, allowed_methods,
                         create_mask=Access.admin,
                         delete_mask=Access.admin,
                         edit_mask=Access.admin,
                         get_mask=Access.admin,
                         query_mask=Access.admin)

    def get_api_name(self):
        return 'user'

    @Rest.route('/login', ['POST'])
    def login(self):
        username = request.form['username']
        password = request.form['password']
        user = auth.authenticate(username, password)
        if user:
            auth.login_user(user)
            return make_status_response('login success', 0)
        else:
            return make_status_response('incorrect username or password', 101)

    @Rest.route('/logout')
    def logout(self):
        auth.logout_user()
        return make_status_response('You are now logged out', 0)

    @Rest.route('/')
    @Access.allow(Access.user)
    def user_detail(self):
        return self.object_detail(auth.get_logged_in_user())

    def read_request_data(self):
        """
        overrides read_request_data() to mask password
        """
        data = request.data or request.form.get('data') or ''
        dt = json.loads(data.decode('utf8'))
        password = dt.get('password')
        if password:
            dt['password'] = make_password(password)
        return dt


api.register(User, UserResource)
