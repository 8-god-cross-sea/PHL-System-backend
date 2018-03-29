import unittest
import datetime
from app.model.inhospital import InHospital
from app.model.patient import Patient

from tests import ResourceTestCase


class InHospitalResourceTestCase(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/inhospital/'
        self.model = InHospital
        self.data = dict(
            patient=1,
            leave_date='',
            status='已入院'
        )
        self.updated = dict(
            patient=1,
            leave_date=str(datetime.datetime.now()),
            status='已出院'
        )
        self.fields = ['patient', 'status']


if __name__ == '__main__':
    unittest.main()
