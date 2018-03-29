import unittest
from app.model import Patient

from tests import ResourceTestCase


class PatientResourceTestCase(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/vaccine/'
        self.model = Patient
        self.data = dict(
            name='测试疫苗',
            price=100,
            count=50
        )
        self.updated = dict(
            name='修改后的测试疫苗',
            price=120,
            count=49
        )
        self.fields = ['name', 'price', 'count']
