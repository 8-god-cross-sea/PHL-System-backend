import unittest
from app.model import Vaccine
from tests import ResourceTestCase
from app.utils import response_manager
import json


class TestPaperResource(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/testpaper/'
        self.model = Vaccine
        self.data = dict(
            name='测试试卷'
        )
        self.updated = dict(
            name='测试试卷m'
        )
        self.fields = ['name']

    @ResourceTestCase.login_as(username='admin', password='admin')
    def test_update_choice(self):
        updated_choices = [2, 1, 6]
        response = self.test_client.put(self.api_url + '1/choice', data=json.dumps(updated_choices),
                                        content_type='application/json')
        self.check_response(response, response_manager.UPDATED_SUCCESS_RESPONSE)
        response = self.get(1)
        actual_choices = []
        for item in self.extract_data(response)['choices']:
            actual_choices.append(item['id'])
        self.assertSetEqual(set(updated_choices), set(actual_choices))
