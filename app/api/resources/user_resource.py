import json

from flask import request
from flask_peewee.utils import make_password

from app import auth
from app.api.api_rest_resource import APIRestResource
from app.api.base_resource import BaseRestResource as Rest
from app.utils import response_manager
from app.api.auth.role_auth import RoleAuth


class UserResource(APIRestResource):
    exclude = ('password', 'permission')
    access_dict = {
        'login': RoleAuth.EVERYONE,
        'logout': RoleAuth.EVERYONE,
        'user_detail': RoleAuth.ANY_USER
    }

    @Rest.route('/login', ['POST'])
    def login(self):
        username = request.json['username']
        password = request.json['password']
        user = auth.authenticate(username, password)
        if user:
            auth.login_user(user)
            return response_manager.LOGIN_SUCCESS_RESPONSE
        else:
            return response_manager.LOGIN_FAILED_RESPONSE

    @Rest.route('/logout')
    def logout(self):
        auth.logout_user()
        return response_manager.LOGOUT_SUCCESS_RESPONSE

    @Rest.route('/me')
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
