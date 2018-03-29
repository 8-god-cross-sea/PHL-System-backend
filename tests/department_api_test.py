import unittest
from app.model.department import Department

from tests import ResourceTestCase


class DepartmentResourceTestCase(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/department/'
        self.model = Department
        self.data = dict(
            name='化验室',
            description='对送验样本进行预处理'
        )
        self.updated = dict(
            name='化验室',
            description='对送验样本进行预处理，生成结果报告'
        )
        self.fields = ['name', 'description']


if __name__ == '__main__':
    unittest.main()
