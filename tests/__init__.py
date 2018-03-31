import functools
import json
import unittest


class TestCaseWithLoginSupport(object):
    """
    Support login & logout for test cases
    """
    test_client = None

    @classmethod
    def setUpClass(cls):
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

    def check_status(self, response, status=200):
        self.assertEqual(response.status_code, status)

    def check_response(self, response, expect):
        self.assertEqual(response.data, expect.data)


class ResourceTestCase(TestCaseWithLoginSupport):
    login_as = TestCaseWithLoginSupport.login_in_as

    def __init__(self, method_name='runTest'):
        from manage import init_db
        init_db()
        super(ResourceTestCase, self).__init__(method_name)
        self.api_url = None
        self.model = None
        self.data = None
        self.updated = None
        self.fields = None

    def check_result(self, expect, response):
        data = self.extract_data(response)
        for field in self.fields:
            self.assertEqual(expect[field], data[field])

    @staticmethod
    def extract_data(response):
        return json.loads(response.data.decode('utf-8'))

    def get(self, pk):
        return self.test_client.get(self.api_url + str(pk))

    def get_list(self):
        return self.test_client.get(self.api_url)

    def create(self, data):
        return self.test_client.post(self.api_url, data=json.dumps(data))

    def update(self, pk, data):
        return self.test_client.put(self.api_url + str(pk), data=json.dumps(data))

    def delete(self, pk):
        return self.test_client.delete(self.api_url + str(pk))

    @login_as(username='admin', password='admin')
    def test_curd_operations(self):
        # test create
        response = self.create(data=self.data)
        self.check_status(response)
        self.check_result(self.data, response)

        # store the pk of created object
        pk = self.extract_data(response)['id']

        # test get list
        response = self.get_list()
        self.check_status(response)
        list_data = self.extract_data(response)
        self.assertTrue(any([obj['id'] == pk for obj in list_data['objects']]))

        # test get before delete
        response = self.get(pk)
        self.check_status(response)
        self.check_result(self.data, response)

        # test update
        response = self.update(pk, self.updated)
        self.check_status(response)
        self.check_result(self.updated, response)

        # test delete
        response = self.delete(pk)
        self.check_status(response)

        # test get after delete
        response = self.get(pk)
        self.check_status(response, 404)

    @login_as('admin', 'admin')
    def test_bad_create(self):
        response = self.create({})
        self.check_status(response, 400)
