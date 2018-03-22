from flask_peewee.rest import RestAPI, Authentication


def setup(app):
    from . import RestAPI_patch
    rest_api = RestAPI(app, default_auth=Authentication(protected_methods=[]))

    # register user api
    from app.model.user import User
    from app.api.resources.user_resource import UserResource
    from app.api.auth.role_auth import RoleAuth
    rest_api.register(User, UserResource, RoleAuth(UserResource.access_dict, RoleAuth.ADMIN))

    rest_api.setup()
