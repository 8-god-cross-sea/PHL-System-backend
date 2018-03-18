import json

from flask import request
from flask_peewee.utils import make_password

from api.access_control import auth
from api.api_rest_resource import APIRestResource
from api.access_control import AccessControl as Access
from api.base_resource import BaseRestResource as Rest
from utils import response_manager


class UserResource(APIRestResource):
    exclude = ('password', 'permission')

    def __init__(self, rest_api, model, authentication, allowed_methods=None):
        super().__init__(rest_api, model, authentication, allowed_methods,
                         create_mask=Access.admin,
                         delete_mask=Access.admin,
                         edit_mask=Access.admin,
                         get_mask=Access.admin,
                         query_mask=Access.admin)

    @Rest.route('/login', ['POST'])
    def login(self):
        username = request.form['username']
        password = request.form['password']
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
