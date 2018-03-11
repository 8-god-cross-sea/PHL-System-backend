from flask_peewee.rest import RestResource
from auth import auth
from flask import request
from functools import wraps


class AuthorizedRestResource(RestResource):

    def get_urls(self):
        return [(url, auth.login_required(func)) for url, func in self.authorized_urls()]

    def authorized_urls(self):
        raise NotImplemented


class BaseRestResource(RestResource):
    url_manager = {}

    @classmethod
    def route(cls, url, method):
        def decorator(func):
            method_dict = cls.url_manager.setdefault(url, {})
            method_dict[method] = func

            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def method_dispatcher(self, get=None, post=None, put=None, delete=None):
        dispatch = {'GET': get, 'POST': post, 'PUT': put, 'DELETE': delete}

        def wrapper(*args, **kwargs):
            return dispatch[request.method](self, *args, **kwargs)

        return wrapper

    @staticmethod
    def rename(new_name):
        def decorator(func):
            func.__name__ = new_name
            return func

        return decorator

    def get_urls(self):
        urls = []
        for key, value in self.url_manager.items():
            f = self.method_dispatcher(
                value.get('GET', None),
                value.get('POST', None),
                value.get('PUT', None),
                value.get('DELETE', None)
            )
            f = self.rename(key)(f)
            urls.append((key, self.require_method(f, list(value.keys()))))
        return urls
