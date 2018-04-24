from playhouse.shortcuts import model_to_dict

from app import auth
from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth
from app.model.report import Report


class ReportResource(APIRestResource):
    default_access = RoleAuth.ADMIN
    access_dict = {
        'my': RoleAuth.ANY_USER
    }

    def get_urls(self):
        return (
            ('/', self.require_method(self.api_list, ['GET'])),
            ('/<pk>', self.require_method(self.api_detail, ['GET'])),
            ('/my', self.require_method(self.my, ['GET'])),

        )

    def my(self):
        # not standardized API
        user = auth.get_logged_in_user()
        return self.response(
            {"meta": {"previous": "", "next": ""},
             "objects": [
                 model_to_dict(report, exclude=(Report.user, Report.exam.test_paper, Report.exam.token), recurse=True)
                 for report in Report.select().where(Report.user == user)]})
