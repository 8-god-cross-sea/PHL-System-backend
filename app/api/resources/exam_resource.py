from app.api.api_rest_resource import APIRestResource


class ExamResource(APIRestResource):
    show_m2m = True
    show_backref = True
