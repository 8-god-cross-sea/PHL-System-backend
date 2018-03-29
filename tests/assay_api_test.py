import unittest
from app.model.assay import Assay

from tests import ResourceTestCase


class AssayResourceTestCase(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/assay/'
        self.model = Assay
        self.data = dict(
            patient=1,
            description='化验的指标'
        )
        self.updated = dict(
            patient=1,
            description='新的化验的指标'
        )
        self.fields = ['patient', 'description']


if __name__ == '__main__':
    unittest.main()
