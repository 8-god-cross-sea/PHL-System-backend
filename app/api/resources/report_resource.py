from app.api.api_rest_resource import APIRestResource


class ReportResource(APIRestResource):
    def get_urls(self):
        return (
            ('/', self.require_method(self.api_list, ['GET'])),
            ('/<pk>', self.require_method(self.api_detail, ['GET'])),
        )
