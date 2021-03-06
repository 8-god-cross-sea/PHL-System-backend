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
        patient = Patient.get_by_id(1)
        self.data = dict(
            patient=patient.id,
            leave_date='',
            status='已入院'
        )
        self.updated = dict(
            patient=patient.id,
            leave_date=str(datetime.datetime.now()),
            status='已出院'
        )
        self.fields = ['status']

    def test_curd_operations(self):
        super().test_curd_operations()


if __name__ == '__main__':
    unittest.main()
