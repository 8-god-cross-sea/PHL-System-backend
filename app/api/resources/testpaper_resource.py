from app.api.api_rest_resource import APIRestResource
from flask_peewee.utils import get_object_or_404
from flask import request
from app.model.choice import Choice
from app.utils.response_manager import UPDATED_SUCCESS_RESPONSE


class TestPaperResource(APIRestResource):
    show_m2m = True

    def get_urls(self):
        return super().get_urls() + (
            ('/<pk>/choices', self.require_method(self.update_choice, ['PUT'])),
        )

    def update_choice(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        to_add = []
        for cid in request.json:
            if Choice.get_or_none(Choice.id == cid):
                to_add.append(cid)
        obj.choices.add(to_add, clear_existing=True)
        return UPDATED_SUCCESS_RESPONSE
