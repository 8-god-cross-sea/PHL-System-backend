from .ResourceBase import BaseRestResource as Rest
from .AccessControl import AccessControl as Access
from flask import Response
from flask_peewee.utils import get_object_or_404


class APIRestResource(Rest):
    __create_mask = Access.user
    __delete_mask = Access.user
    __edit_mask = Access.user
    __single_mask = Access.user
    __query_mask = Access.user

    @Rest.route('/', ['POST', 'PUT'])
    @Access.allow(__create_mask)
    def create_obj(self):
        try:
            ret = self.create()
        except Exception as e:
            return Response(str(e), 400)
        return ret

    @Rest.route('/<pk>', ['GET'])
    @Access.allow(__single_mask)
    def edit_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.object_detail(obj)

    @Rest.route('/<pk>', ['POST', 'PUT'])
    @Access.allow(__delete_mask)
    def edit_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.edit(obj)

    @Rest.route('/<pk>', ['DELETE'])
    @Access.allow(__edit_mask)
    def delete_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.delete(obj)

    @Rest.route('/list')
    @Access.allow(__query_mask)
    def api_list(self):
        return self.object_list()
