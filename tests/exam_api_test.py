import json
import unittest

from app.model import Exam
from app.utils import response_manager
from tests import ResourceTestCase
from tests import TestCaseWithLoginSupport


class ExamResourceTest(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/exam/'
        self.model = Exam
        self.data = dict(
            test_paper=1,
            name='test exam',
            duration=60,
            start='2018-04-25 22:22:00'
        )
        self.updated = dict(
            test_paper=2,
            name='test exam1',
            duration=90,
            start='2018-04-25 22:22:10'
        )
        self.fields = ['name', 'duration', 'start']

    @TestCaseWithLoginSupport.login_in_as('user', 'user')
    def test_my_exam(self):
        response = self.test_client.get('/api/exam/my')
        self.check_status(response)

    @TestCaseWithLoginSupport.login_in_as('user', 'user')
    def test_exam(self):
        response = self.test_client.get('/api/exam/begin?eid=2')
        token = json.loads(response.data)['token']
        data = {'answers': [0, 0, 0], 'token': token, 'eid': 1}

        # submit a wrong eid
        response = self.test_client.post('/api/exam/submit', data=json.dumps(data), content_type='application/json')
        self.check_response_and_status(response, response_manager.NOT_PERMITTED_RESPONSE, 403)

        # correctly submit
        data['eid'] = 2
        response = self.test_client.post('/api/exam/submit', data=json.dumps(data), content_type='application/json')
        self.check_status(response)
        score = json.loads(response.data)['score']
        self.assertIsNotNone(score)

        # submit twice
        response = self.test_client.post('/api/exam/submit', data=json.dumps(data), content_type='application/json')
        self.check_response_and_status(response, response_manager.ALREADY_TAKEN_EXAM_RESPONSE, 202)

    @TestCaseWithLoginSupport.login_in_as('admin', 'admin')
    def test_not_his_exam(self):
        response = self.test_client.get('/api/exam/begin?eid=2')
        self.check_response_and_status(response, response_manager.NOT_PERMITTED_RESPONSE, 403)

    @TestCaseWithLoginSupport.login_in_as('user', 'user')
    def test_already_taken_exam(self):
        response = self.test_client.get('/api/exam/begin?eid=1')
        self.check_response_and_status(response, response_manager.ALREADY_TAKEN_EXAM_RESPONSE, 202)


if __name__ == '__main__':
    unittest.main()
