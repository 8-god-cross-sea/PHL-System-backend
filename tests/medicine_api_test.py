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
            stock=20
        )
        self.updated = dict(
            name='drug',
            price=30,
            stock=30
        )
        self.fields = ['name', 'price', 'stock']


if __name__ == '__main__':
    unittest.main()
