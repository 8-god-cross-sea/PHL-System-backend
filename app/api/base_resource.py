from flask_peewee.rest import RestResource
from flask import request


class BaseRestResource(RestResource):
    url_manager = {}

    @classmethod
    def route(cls, url, methods=['GET']):
        """route url mapping for resources

        :param url: url for visiting resources
        :param methods: a list containing allowed HTTP method
        :return:
        """

        def decorator(func):
            method_dict = cls.url_manager.setdefault(url, {})
            method_dict.update({key: func for key in methods})
            return func

        return decorator

    def method_dispatcher(self, **method_dict):
        def wrapper(*args, **kwargs):
            return method_dict[request.method](self, *args, **kwargs)

        return wrapper

    @staticmethod
    def rename(new_name):
        def decorator(func):
            func.__name__ = new_name
            return func

        return decorator

    def get_urls(self):
        """dynamically create url mapping.

        Use a method dispatcher to create function. The name of the function needs to be restored since RestResource use
        function.__name__ to create view mapping. Note that the origin get_urls() in RestResource cannot dispatch
        multiple method for single entry, only the first registered method's name will be treated as the mapping name.
        """
        urls = []
        for key, dispatcher in self.url_manager.items():
            f = self.method_dispatcher(**dispatcher)
            f = self.rename(next(iter(dispatcher.values())).__name__)(f)            # use first function name
            urls.append((key, self.require_method(f, list(dispatcher.keys()))))
        return urls
