import unittest
from app.model.role import Role

from tests import ResourceTestCase


class RoleResourceTestCase(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/role/'
        self.model = Role
        self.data = dict(
            name='角色',
            description='角色的描述'
        )
        self.updated = dict(
            name='角色m',
            description='角色的描述m'
        )
        self.fields = ['name', 'description']


if __name__ == '__main__':
    unittest.main()
