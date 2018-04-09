import unittest
from app.model.case import Case

from tests import ResourceTestCase


class CaseResourceTestCase(ResourceTestCase, unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super().__init__(method_name)
        self.api_url = '/api/case/'
        self.model = Case
        self.data = dict(
            name='疾病名称',
            reception='接诊',
            inspection='检查',
            result='诊断',
            treatment='治疗'
        )
        self.updated = dict(
            name='疾病名称m',
            reception='接诊m',
            inspection='检查m',
            result='诊断m',
            treatment='治疗m'
        )
        self.fields = ['name']
