from flask_peewee.rest import RestAPI, Authentication


def setup(app):
    rest_api = RestAPI(app, default_auth=Authentication(protected_methods=[]))

    # register user api
    from app.model.user import User
    from app.api.resources.user_resource import UserResource
    rest_api.register(User, UserResource)

    rest_api.setup()

