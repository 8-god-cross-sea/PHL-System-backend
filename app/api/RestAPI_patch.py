import functools
from flask_peewee.rest import RestAPI
from app.utils import response_manager


def auth_wrapper(self, func, provider):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not provider.authorize(func.__name__):
            return response_manager.NOT_PERMITTED_RESPONSE
        return func(*args, **kwargs)

    return inner


RestAPI.auth_wrapper = auth_wrapper
