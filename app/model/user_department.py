from app.model.user import User
from app.model.department import Department
from peewee import *
from app import db


class UserDepartment(db.model):
    user = ForeignKeyField(User)
    department = ForeignKeyField(Department)
