import unittest
from tests import TestCaseWithLoginSupport


class ReportResourceTest(TestCaseWithLoginSupport, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        from manage import init_db
        init_db()

    @TestCaseWithLoginSupport.login_in_as('user', 'user')
    def test_my_report(self):
        response = self.test_client.get('/api/report/my')
        self.check_status(response)


if __name__ == '__main__':
    unittest.main()
