import functools

from flask_peewee.auth import Auth
import phl_app
from model import db
from model.user import User
from utils import response_manager

auth = Auth(phl_app.app, db, user_model=User)


class AccessControl:
    everyone = 0
    user = 1
    front = 2
    assist = 4
    doctor = 8
    admin = 16

    @classmethod
    def allow(cls, *args):
        return cls._check_permission(
            lambda permission: (0 in args) or any([to_check & permission for to_check in args]))

    @classmethod
    def at_least(cls, to_check):
        return cls._check_permission(lambda permission: to_check <= permission)

    @classmethod
    def _check_permission(cls, check):
        """

        :param to_check: an integer to check permission, each bit represents a role
        :param check: a function to check the permission, return true if ok. (to_check, user_vector) -> bool
        :return: a decorator wraps request handler function and do the access control before calling the handler
        """

        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                user = auth.get_logged_in_user()
                permission = user.permission if user else 0
                if check(permission):
                    return func(*args, **kwargs)
                else:
                    return response_manager.NOT_PERMITTED_RESPONSE

            return wrapper

        return decorator