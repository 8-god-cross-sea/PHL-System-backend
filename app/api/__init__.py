from flask_peewee.rest import RestAPI, Authentication

from app.api.auth.role_auth import RoleAuth
from app.model import *
from app.api.resources import *


def register_api(rest_api, model, rest_resource):
    rest_api.register(model, rest_resource, RoleAuth(rest_resource.access_dict or {}, rest_resource.default_access))


def setup(app):
    from . import RestAPI_patch
    rest_api = RestAPI(app, default_auth=Authentication(protected_methods=[]))

    # register user api
    register_api(rest_api, User, UserResource)
    register_api(rest_api, InHospital, InHospitalResource)
    register_api(rest_api, Department, DepartmentResource)
    register_api(rest_api, Medicine, MedicineResource)
    register_api(rest_api, Vaccine, VaccineResource)
    register_api(rest_api, Patient, PatientResource)
    register_api(rest_api, Assay, AssayResource)
    rest_api.setup()
