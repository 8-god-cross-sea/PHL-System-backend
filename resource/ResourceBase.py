from flask_peewee.rest import RestResource
from auth import auth


class AuthorizedRestResource(RestResource):

    def get_urls(self):
        return [(url, auth.login_required(func)) for url, func in self.authorized_urls()]

    def authorized_urls(self):
        raise NotImplemented
