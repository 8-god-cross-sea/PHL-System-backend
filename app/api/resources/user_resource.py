import json

from flask import request
from flask_peewee.utils import make_password

from app import auth
from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth
from app.utils import response_manager
from app.model.user import User


class UserResource(APIRestResource):
    exclude = (User.password, User.permission)
    default_access = RoleAuth.ADMIN

    access_dict = {
        'login': RoleAuth.EVERYONE,
        'logout': RoleAuth.EVERYONE,
        'user_detail': RoleAuth.ANY_USER
    }

    def get_urls(self):
        return super().get_urls() + (
            ('/login', self.require_method(self.login, ['POST'])),
            ('/logout', self.require_method(self.logout, ['GET'])),
            ('/me', self.require_method(self.user_detail, ['GET'])),
        )

    def login(self):
        username = request.json['username']
        password = request.json['password']
        user = auth.authenticate(username, password)
        if user:
            auth.login_user(user)
            return response_manager.LOGIN_SUCCESS_RESPONSE
        else:
            return response_manager.LOGIN_FAILED_RESPONSE

    def logout(self):
        auth.logout_user()
        return response_manager.LOGOUT_SUCCESS_RESPONSE

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
