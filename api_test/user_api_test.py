import unittest
import json

from api_test import TestCaseWithLoginSupport


class UserApiTestCase(TestCaseWithLoginSupport):
    login_in_as = TestCaseWithLoginSupport.login_in_as

    @login_in_as(username='admin', password='admin')
    def test_user_detail(self):
        recv = self.test_client.get('/api/user/1')
        self.assertEqual(recv.status_code, 200)

        data = json.loads(next(recv.response).decode('utf-8'))
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['username'], 'admin')
        self.assertEqual(data['email'], 'admin@admin.com')
        self.assertEqual(data['active'], True)


if __name__ == '__main__':
    unittest.main()
