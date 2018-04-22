import unittest
from app.model import Vaccine
from tests import ResourceTestCase


class VaccineResource(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/vaccine/'
        self.model = Vaccine
        self.data = dict(
            name='一个药',
            price=60,
            count=50
        )
        self.updated = dict(
            name='一个假药',
            price=61,
            count=52
        )
        self.fields = ['name', 'price', 'count']
