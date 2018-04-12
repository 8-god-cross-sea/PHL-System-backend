from flask_peewee.utils import get_object_or_404
from app.api.api_rest_resource import APIRestResource


class CaseResource(APIRestResource):
    exclude = ('reception', 'inspection', 'result', 'treatment')

    def get_obj(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        s = self.get_serializer()
        data = self.prepare_data(
            obj, s.serialize_object(obj, self._fields, {})
        )
        return self.response(data)
