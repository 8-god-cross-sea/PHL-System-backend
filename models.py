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
    admin = BooleanField(default=False)


tables = [cls for cls in db.Model.__subclasses__()]

if __name__ == '__main__':
    User.create_table()
    User.create(username='admin', password='admin', email='admin@admin.com')
