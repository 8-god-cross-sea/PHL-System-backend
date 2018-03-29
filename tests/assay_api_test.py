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
            wbc=6.8,
            rbc=4.9,
            plt=245
        )
        self.updated = dict(
            patient=1,
            wbc=5.8,
            rbc=7.3,
            plt=211
        )
        self.fields = ['patient', 'wbc', 'rbc', 'plt']


if __name__ == '__main__':
    unittest.main()
