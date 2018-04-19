from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth
from flask_peewee.utils import get_object_or_404
from app import auth
from flask import request
from playhouse.shortcuts import model_to_dict
from app.model.choice import Choice
from flask_peewee.utils import make_password, check_password
from app.utils.response_manager import NOT_PERMITTED_RESPONSE


class ExamResource(APIRestResource):
    default_access = RoleAuth.ADMIN
    access_dict = {
        'my_exams': RoleAuth.ANY_USER,
        'begin_exam': RoleAuth.ANY_USER
    }

    def get_urls(self):
        return super().get_urls() + (
            ('/begin', self.require_method(self.begin_exam, ['GET'])),
            ('/my', self.require_method(self.my_exams, ['GET'])),
        )

    def make_token(self, exam):
        return make_password(str(exam.id) + str(exam.token))

    def check_token(self, exam, token):
        return check_password(str(exam.id) + str(exam.token), token)

    def my_exams(self):
        user = auth.get_logged_in_user()
        # user = User.get_by_id(2)
        return self.response({"objects": [model_to_dict(exam, exclude=self.always_exclude) for exam in user.exams]})

    def begin_exam(self):
        eid = request.args.get('eid')
        user = auth.get_logged_in_user()
        # user = User.get_by_id(3)
        exam = get_object_or_404(self.get_query(), self.pk == eid)
        print(eid)
        print(exam.users)
        if user in exam.users:
            choices = exam.test_paper.choices
            response = {
                'problem': [model_to_dict(choice, exclude=(Choice.answer, Choice.case_type, Choice.id)) for choice in
                            choices],
                'token': self.make_token(exam)
            }
            return self.response(response)
        else:
            return NOT_PERMITTED_RESPONSE
