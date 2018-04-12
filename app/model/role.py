from peewee import *
from app import db


class Role(db.Model):
    name = CharField()
    description = TextField()
