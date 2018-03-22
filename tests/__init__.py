import json
import unittest
import functools

from app.utils import response_manager


class TestCaseWithLoginSupport(unittest.TestCase):
    """
    Support login & logout for test cases
    """
    test_client = None

    @classmethod
    def setUpClass(cls):
        from manage import init_db
        init_db()

        from app import app
        cls.test_client = app.test_client()

    @classmethod
    def login(cls, username, password):
        return cls.test_client.post('/api/user/login', data=json.dumps(dict(
            username=username,
            password=password
        )), content_type='application/json', follow_redirects=True)

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


class ResourceTestCase(TestCaseWithLoginSupport):
    login_as = TestCaseWithLoginSupport.login_in_as

    def __init__(self, method_name='runTest'):
        super(ResourceTestCase, self).__init__(method_name)
        self.api_url = None
        self.model = None
        self.data = None
        self.updated = None
        self.fields = None

    def check_result(self, expect, actual):
        for field in self.fields:
            self.assertEqual(expect[field], actual[field])

    def check_status(self, response, status=200):
        self.assertEqual(response.status_code, status)

    @staticmethod
    def get_data(response):
        return json.loads(response.data.decode('utf-8'))

    def get(self, id):
        return self.test_client.get(self.api_url + str(id))

    def get_list(self):
        return self.test_client.get(self.api_url)

    def create(self, data):
        return self.test_client.post(self.api_url, data=json.dumps(data))

    def update(self, id, data):
        return self.test_client.put(self.api_url + str(id), data=json.dumps(data))

    def delete(self, id):
        return self.test_client.delete(self.api_url + str(id))

    @login_as(username='admin', password='admin')
    def basic_operations(self):

        # test create
        response = self.create(data=self.data)
        self.check_status(response)
        data = self.get_data(response)
        self.check_result(self.data, data)

        # store the id of created object
        id = data['id']

        # test get list
        response = self.get_list()
        self.check_status(response)
        data = self.get_data(response)
        self.assertTrue(any([obj['id'] == id for obj in data['objects']]))

        # test update
        response = self.update(id, self.updated)
        self.check_status(response)
        data = self.get_data(response)
        self.check_result(self.updated, data)

        # test delete
        response = self.delete(id)
        self.check_status(response)

        # test get
        response = self.get(id)
        self.check_status(response, 404)







