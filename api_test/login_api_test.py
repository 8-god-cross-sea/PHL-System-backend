import unittest

from api_test import TestCaseWithLoginSupport
from utils import response_manager


class LoginApiTestCase(TestCaseWithLoginSupport):

    def test_login(self):
        expect = response_manager.LOGIN_SUCCESS_RESPONSE
        recv = self.login('admin', 'admin')

        self.assertEqual(recv.status_code, expect.status_code)
        self.assertEqual(list(recv.response), list(expect.response))

    def test_logout(self):
        expect = response_manager.LOGOUT_SUCCESS_RESPONSE
        recv = self.logout()

        self.assertEqual(recv.status_code, expect.status_code)
        self.assertListEqual(list(recv.response), list(expect.response))


if __name__ == '__main__':
    unittest.main()
