from .base_resource import BaseRestResource as Rest
from flask import Response
from flask_peewee.utils import get_object_or_404


class APIRestResource(Rest):
    def get_api_name(self):
        return self.model.__name__.lower()

    @Rest.route('/', ['POST', ' PUT'])
    def root(self):
        try:
            ret = self.create()
        except Exception as e:
            return Response(str(e), 400)
        return ret

    @Rest.route('/<pk>', ['GET'])
    def get_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.object_detail(obj)

    @Rest.route('/<pk>', ['POST', 'PUT'])
    def edit_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.edit(obj)

    @Rest.route('/<pk>', ['DELETE'])
    def delete_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.delete(obj)

    @Rest.route('/list')
    def api_list(self):
        return self.object_list()
