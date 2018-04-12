from flask_peewee.utils import get_object_or_404
from app.api.api_rest_resource import APIRestResource
from app.model.case import Case


class CaseResource(APIRestResource):
    exclude = (Case.inspection, Case.reception, Case.result, Case.treatment)

    def api_detail(self, pk, methods=None):
        backup = self.exclude
        self.exclude = ()
        response = super().api_detail(pk, methods)
        self.exclude = backup
        return response
