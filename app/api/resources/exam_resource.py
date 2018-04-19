from flask import request
from flask_peewee.utils import get_object_or_404
from flask_peewee.utils import make_password, check_password
from playhouse.shortcuts import model_to_dict

from app import auth
from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth
from app.model.choice import Choice
from app.model.report import Report
from app.model.user import User
from app.utils.response_manager import NOT_PERMITTED_RESPONSE, ALREADY_TAKEN_EXAM_RESPONSE


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
            ('/submit', self.require_method(self.submit, ['POST'])),
        )

    def make_token(self, exam):
        return make_password(str(exam.id) + str(exam.token))

    def check_token(self, exam, token):
        return check_password(str(exam.id) + str(exam.token), token)

    def my_exams(self):
        user = auth.get_logged_in_user()
        return self.response({"objects": [model_to_dict(exam, exclude=self.always_exclude) for exam in user.exams]})

    def begin_exam(self):
        eid = request.args.get('eid')
        user = auth.get_logged_in_user()
        exam = get_object_or_404(self.get_query(), self.pk == eid)
        if user in exam.users:
            if self.already_taken(user, exam):
                return ALREADY_TAKEN_EXAM_RESPONSE
            else:
                choices = exam.test_paper.choices
                response = {
                    'problem': [model_to_dict(choice, exclude=(Choice.answer, Choice.case_type, Choice.id)) for choice
                                in choices],
                    'token': self.make_token(exam)
                }
                return self.response(response)
        else:
            return NOT_PERMITTED_RESPONSE

    def submit(self):
        eid = request.json['eid']
        token = request.json['token']
        answers = request.json['answers']
        user = auth.get_logged_in_user()
        exam = get_object_or_404(self.get_query(), self.pk == eid)
        if self.check_token(exam, token):
            if self.already_taken(user, exam):
                return ALREADY_TAKEN_EXAM_RESPONSE
            else:
                choices = exam.test_paper.choices
                counter = 0
                for idx, choice in enumerate(choices):
                    counter += choice.answer == answers[idx]
                score = counter / len(choices) * 100
                report = Report.create(user=user, exam=exam, score=score)
                return self.response(model_to_dict(report, only=(Report.score,)))
        else:
            return NOT_PERMITTED_RESPONSE

    def already_taken(self, user, exam):
        return Report.select().where((Report.user == user) & (Report.exam == exam))
