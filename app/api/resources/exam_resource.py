from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth
from flask_peewee.utils import get_object_or_404
from app import auth
from flask import request
from app.model.user import User
from app.model.exam import Exam


class ExamResource(APIRestResource):
    default_access = RoleAuth.ADMIN
    show_m2m = True
    show_backref = True

    def get_urls(self):
        return super().get_urls() + (
            ('/begin', self.require_method(self.begin_exam, ['GET'])),
        )

    def begin_exam(self):
        eid = request.args.get('eid')
        user = auth.get_logged_in_user()
        exam = get_object_or_404(self.get_query(), self.pk == eid)
        print(eid)
        print(exam.users)
        if user in exam.users:
            return self.response({'1'})
        else:
            return self.response({'0'})
