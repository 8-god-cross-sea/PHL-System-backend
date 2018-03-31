import unittest
from tests import TestCaseWithLoginSupport


class ApiOverviewResourceTest(TestCaseWithLoginSupport, unittest.TestCase):
    def test_api_overview(self):
        response = self.test_client.get('/api')
        self.check_status(response)

    def test_api_over_view_with_redirect(self):
        response = self.test_client.get('/')
        self.check_status(response, 302)
        response = self.test_client.get('/', follow_redirects=True)
        self.check_status(response)
