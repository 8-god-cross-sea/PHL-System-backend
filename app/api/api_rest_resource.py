import json
from flask import request
from flask import Response
from flask import abort
from werkzeug.exceptions import *
from flask_peewee.rest import RestResource
from peewee import PeeweeException
from playhouse.shortcuts import model_to_dict

from app import model
from app.api.auth.role_auth import RoleAuth
from app.model.user import User
from app.model.exam import Exam


class APIRestResource(RestResource):
    default_access = RoleAuth.ANY_USER
    show_m2m = False
    show_backref = False
    access_dict = {}
    always_exclude = (User.password, User.permission, Exam.token)
    exclude = ()

    def get_urls(self):
        return (
            ('/', self.require_method(self.api_list, ['GET', 'POST'])),
            ('/<pk>', self.require_method(self.api_detail, ['GET', 'POST', 'PUT', 'DELETE'])),
        )

    @classmethod
    def get_model(cls):
        return getattr(model, cls.__name__[:-8])

    def get_api_name(self):
        return self.model.__name__.lower()

    def authorize(self, name):
        return self.authentication.authorize(name)

    def api_list(self):
        try:
            return super().api_list()
        except (HTTPException, PeeweeException) as e:
            abort(400, e)

    def api_detail(self, pk, method=None):
        return super().api_detail(pk, method)

    def prepare_data(self, obj, data):
        return model_to_dict(obj, exclude=self.always_exclude + self.exclude, manytomany=self.show_m2m,
                             backrefs=self.show_backref)

    def response(self, data):
        kwargs = {} if request.is_xhr else {'indent': 2}
        return Response(json.dumps(data, **kwargs, default=str), mimetype='application/json')
