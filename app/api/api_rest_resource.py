from flask import abort
from werkzeug.exceptions import *
from flask_peewee.rest import RestResource
from peewee import PeeweeException

from app import model
from app.api.auth.role_auth import RoleAuth


class APIRestResource(RestResource):
    default_access = RoleAuth.ANY_USER
    access_dict = {}

    def get_urls(self):
        return (
            ('/', self.require_method(self.api_list, ['GET', 'POST'])),
            ('/<pk>', self.require_method(self.api_detail, ['GET', 'POST', 'PUT', 'DELETE'])),
        )

    @classmethod
    def get_model(cls):
        return getattr(model, cls.__name__[:-8])

    def get_api_name(self):
        return self.model.__name__.lower()

    def authorize(self, name):
        return self.authentication.authorize(name)

    def api_list(self):
        try:
            return super().api_list()
        except HTTPException as e:
            raise e
        except PeeweeException:
            abort(400)

    def api_detail(self, pk, method=None):
        try:
            return super().api_detail(pk, method)
        except HTTPException as e:
            raise e
        except PeeweeException:
            abort(400)

