import datetime

from flask_peewee.auth import BaseUser
from peewee import *
from app import db


class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    permission = IntegerField(default=1)
