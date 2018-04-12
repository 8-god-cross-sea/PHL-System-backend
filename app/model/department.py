from peewee import *
from app import db
from app.model.user import User


class Department(db.Model):
    name = CharField()
    description = CharField()

    users = ManyToManyField(User, backref='departments')
