from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth


class PatientResource(APIRestResource):
    default_access = RoleAuth.ANY_USER
