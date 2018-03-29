import unittest
from app.model import Vaccine
from tests import ResourceTestCase


class VaccineResource(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/patient/'
        self.model = Vaccine
        self.data = dict(
            name='测试狗',
            description='用来测试的测试狗'
        )
        self.updated = dict(
            name='软件狗',
            description='用来测试的软件狗'
        )
        self.fields = ['name', 'description']