from .ResourceBase import BaseRestResource as Rest
from .ResponseManager import make_status_response
from auth import auth
from models import User
from api import api
from flask import request, Response
import json
from flask_peewee.utils import make_password
from flask_peewee.utils import get_object_or_404


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
            return make_status_response('login success', 0)
        else:
            return make_status_response('incorrect username or password', 101)

    @Rest.route('/logout')
    def logout(self):
        auth.logout_user()
        return make_status_response('You are now logged out', 0)

    @Rest.route('/')
    @Rest.permission()
    def user_detail(self):
        return self.object_detail(auth.get_logged_in_user())

    @Rest.route('/', ['POST', 'PUT'])
    @Rest.permission(__user_admin_mask)
    def create_user(self):
        try:
            ret = self.create()
        except Exception as e:
            return Response(str(e), 400)
        return ret

    @Rest.route('/<string:username>', ['POST', 'PUT'])
    @Rest.permission()
    def edit_user(self, username):
        obj = get_object_or_404(self.get_query(), User.username == username)
        return self.edit(obj)

    @Rest.route('/<string:username>', ['DELETE'])
    @Rest.permission(__user_admin_mask)
    def delete_user(self, username):
        obj = get_object_or_404(self.get_query(), User.username == username)
        return self.delete(obj)

    @Rest.route('/list')
    @Rest.permission(__user_admin_mask)
    def api_list(self):
        return self.object_list()

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
