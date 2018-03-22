import unittest

from tests import ResourceTestCase
from app.model.user import User


class UserResourceTestCast(ResourceTestCase):

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

    def test_basic_operations(self):
        self.basic_operations()


if __name__ == '__main__':
    unittest.main()
