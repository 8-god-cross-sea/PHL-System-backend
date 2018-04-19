from app.api.api_rest_resource import APIRestResource
from flask_peewee.utils import get_object_or_404
from flask import request
from app.utils.response_manager import UPDATED_SUCCESS_RESPONSE


class TestPaperResource(APIRestResource):
    show_m2m = True

    def get_urls(self):
        return super().get_urls() + (
            ('/<pk>/choice', self.require_method(self.update_choice, ['PUT'])),
        )

    def update_choice(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        obj.choices.clear()
        obj.choices.add(request.json)
        return UPDATED_SUCCESS_RESPONSE
