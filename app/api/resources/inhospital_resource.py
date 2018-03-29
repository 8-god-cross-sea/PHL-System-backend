from app.api.api_rest_resource import APIRestResource
from app.api.auth.role_auth import RoleAuth


class InHospitalResource(APIRestResource):
    default_access = RoleAuth.EVERYONE
