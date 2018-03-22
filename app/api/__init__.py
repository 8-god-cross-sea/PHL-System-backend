from flask_peewee.rest import RestAPI, Authentication
from app.api.auth.role_auth import RoleAuth


def register_api(rest_api, model, rest_resource, role_mask=RoleAuth.EVERYONE):
    rest_api.register(model, rest_resource, RoleAuth(rest_resource.access_dict or {}, role_mask))


def setup(app):
    from . import RestAPI_patch
    rest_api = RestAPI(app, default_auth=Authentication(protected_methods=[]))

    # register user api
    from app.model.user import User
    from app.api.resources.user_resource import UserResource
    register_api(rest_api, User, UserResource, RoleAuth.ADMIN)

    rest_api.setup()
