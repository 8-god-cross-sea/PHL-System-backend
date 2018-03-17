from flask_peewee.rest import RestAPI, Authentication


def setup(app):
    rest_api = RestAPI(app, default_auth=Authentication(protected_methods=[]))

    # register user api
    from model.user import User
    from api.resources.user_resource import UserResource
    rest_api.register(User, UserResource)

    rest_api.setup()

