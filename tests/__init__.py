import os
import unittest
import functools


class TestCaseWithLoginSupport(unittest.TestCase):
    """
    Support login & logout for test cases
    """
    test_client = None

    @classmethod
    def setUpClass(cls):
        from app import app
        cls.test_client = app.test_client()

        from manage import init_db
        init_db()

    @classmethod
    def login(cls, username, password):
        return cls.test_client.post('/api/user/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    @classmethod
    def logout(cls):
        return cls.test_client.get('/api/user/logout')

    @classmethod
    def login_in_as(cls, username, password):

        def _(func):
            @functools.wraps(func)
            def wrap_login_logout(self, *args, **kwargs):
                self.login(username=username, password=password)
                func(self, *args, **kwargs)
                self.logout()
            return wrap_login_logout

        return _

