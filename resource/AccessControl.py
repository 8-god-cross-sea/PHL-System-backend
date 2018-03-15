import functools

from auth import auth
from .ResponseManager import make_status_response


class AccessControl:
    everyone = 0
    user = 1
    front = 2
    assist = 4
    doctor = 8
    admin = 16

    @classmethod
    def allow(cls, *args):
        return cls.check_permission(lambda permission: any([to_check & permission for to_check in args]))

    @classmethod
    def at_least(cls, to_check):
        return cls.check_permission(lambda permission: to_check < permission)

    @classmethod
    def check_permission(cls, check):
        """

        :param to_check: an integer to check permission, each bit represents a role
        :param check: a function to check the permission, return true if ok. (to_check, user_vector) -> bool
        :return: a decorator wraps request handler function and do the access control before calling the handler
        """
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                user = auth.get_logged_in_user()
                if not user:
                    return make_status_response('Login required', 101)
                if check(user.permission):
                    return func(*args, **kwargs)
                else:
                    return make_status_response('Not permitted', 101)

            return wrapper
        return decorator
