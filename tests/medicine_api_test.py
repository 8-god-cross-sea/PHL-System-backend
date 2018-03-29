import unittest
from app.model.medicine import Medicine

from tests import ResourceTestCase


class MedicineResourceTestCase(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/medicine/'
        self.model = Medicine
        self.data = dict(
            name='drug',
            price=20,
            count=20
        )
        self.updated = dict(
            name='drug',
            price=30,
            count=30
        )
        self.fields = ['name', 'price', 'count']


if __name__ == '__main__':
    unittest.main()
