import unittest

from app.model.user import User
from app.utils import response_manager
from tests import ResourceTestCase


class UserResourceTestCast(ResourceTestCase, unittest.TestCase):

    def __init__(self, method_name='runTest'):
        super(UserResourceTestCast, self).__init__(method_name)
        self.api_url = '/api/user/'
        self.model = User
        self.data = dict(
            username='test_user',
            password='test_password',
            email='test@test.com',
            permission=0b10000
        )
        self.updated = dict(
            username='test_update_user',
            password='test_password',
            email='test_update@test.com',
            permission=0b10000
        )
        self.fields = ['username', 'email']

    def test_login_success(self):
        response = self.login('admin', 'admin')
        self.check_response(response, response_manager.LOGIN_SUCCESS_RESPONSE)

    def test_login_failed(self):
        response = self.login('admin', 'wrong_password')
        self.check_response(response, response_manager.LOGIN_FAILED_RESPONSE)

    def test_logout(self):
        response = self.logout()
        self.check_response(response, response_manager.LOGOUT_SUCCESS_RESPONSE)

    @ResourceTestCase.login_as('user', 'user')
    def test_me(self):
        response = self.test_client.get(self.api_url + 'me')
        self.check_status(response)


if __name__ == '__main__':
    unittest.main()
