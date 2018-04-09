from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth


class CaseResource(APIRestResource):
    exclude = ('reception', 'inspection', 'result', 'treatment')
    default_access = RoleAuth.ANY_USER
