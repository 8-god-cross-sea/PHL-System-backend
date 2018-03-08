from flask_peewee.rest import RestResource

from auth import user_auth
from models import User
from api import api


class UserResource(RestResource):
    exclude = ('password', 'email',)

    def get_api_name(self):
        return 'user'

    def get_urls(self):
        return [
            ('/<pk>', self.api_detail),
            ('/list', self.api_list)
        ]


api.register(User, UserResource, auth=user_auth)
