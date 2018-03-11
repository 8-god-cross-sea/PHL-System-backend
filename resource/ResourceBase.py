from flask_peewee.rest import RestResource
from auth import auth
from flask import request, Response
import functools


class BaseRestResource(RestResource):
    url_manager = {}

    @classmethod
    def route(cls, url, method=['GET']):
        """route url mapping for resources

        :param url: url for visiting resources
        :param method: a list containing allowed HTTP method
        :return:
        """

        def decorator(func):
            method_dict = cls.url_manager.setdefault(url, {})
            method_dict.update({key: func for key in method})
            return func

        return decorator

    @classmethod
    def permission(cls, mod=0):
        """set control permission for the specific resources

        :param mod: an integer indicates permission
        :return: decorator
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                user = auth.get_logged_in_user()
                if user and (not mod or mod & user.permission):
                    return func(*args, **kwargs)
                else:
                    return Response('Forbidden', 403)

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
                value.get('GET'),
                value.get('POST'),
                value.get('PUT'),
                value.get('DELETE')
            )
            f = self.rename(key)(f)  # this rename method avoids view mapping overriding error
            urls.append((key, self.require_method(f, list(value.keys()))))
        return urls
