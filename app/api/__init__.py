from flask_peewee.rest import RestAPI, Authentication

from app.api.auth.role_auth import RoleAuth
from app.api.api_rest_resource import APIRestResource
from app.api.resources import *


def register_api(rest_api, rest_resource):
    rest_api.register(rest_resource.get_model(), rest_resource,
                      RoleAuth(rest_resource.access_dict or {}, rest_resource.default_access))


def setup(app):
    from . import RestAPI_patch
    rest_api = RestAPI(app, default_auth=Authentication(protected_methods=[]))

    # register user api
    for api in APIRestResource.__subclasses__():
        register_api(rest_api, api)
    rest_api.setup()
