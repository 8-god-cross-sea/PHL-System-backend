from flask_peewee.utils import get_object_or_404

from app.api.auth.role_auth import RoleAuth
from app.utils import response_manager
from .base_resource import BaseRestResource as Rest


class APIRestResource(Rest):
    default_access = RoleAuth.EVERYONE

    def get_api_name(self):
        return self.model.__name__.lower()

    @Rest.route('/')
    def api_list(self):
        return self.object_list()

    @Rest.route('/', ['POST', ' PUT'])
    def root(self):
        try:
            ret = self.create()
        except Exception as e:
            return response_manager.make_bad_request_response(str(e))
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
