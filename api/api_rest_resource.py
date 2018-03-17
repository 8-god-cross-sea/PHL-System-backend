from .base_resource import BaseRestResource as Rest
from .access_control import AccessControl as Access
from flask import Response
from flask_peewee.utils import get_object_or_404


class APIRestResource(Rest):

    def __init__(self, rest_api, model, authentication, allowed_methods=None, create_mask=Access.user,
                 delete_mask=Access.user, edit_mask=Access.user,
                 get_mask=Access.user, query_mask=Access.user):
        APIRestResource.create_obj = Rest.route('/', ['POST', 'PUT'])(
            Access.allow(create_mask)(APIRestResource.create_obj))
        APIRestResource.get_obj = Rest.route('/<pk>', ['GET'])(
            Access.allow(get_mask)(APIRestResource.get_obj))
        APIRestResource.edit_obj = Rest.route('/<pk>', ['POST', 'PUT'])(
            Access.allow(edit_mask)(APIRestResource.edit_obj))
        APIRestResource.delete_obj = Rest.route('/<pk>', ['DELETE'])(
            Access.allow(delete_mask)(APIRestResource.delete_obj))
        APIRestResource.api_list = Rest.route('/list')(
            Access.allow(query_mask)(APIRestResource.api_list))
        super().__init__(rest_api, model, authentication, allowed_methods)

    def get_api_name(self):
        return self.model.__name__.lower()

    def create_obj(self):
        try:
            ret = self.create()
        except Exception as e:
            return Response(str(e), 400)
        return ret

    def get_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.object_detail(obj)

    def edit_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.edit(obj)

    def delete_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.delete(obj)

    def api_list(self):
        return self.object_list()
