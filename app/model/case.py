from peewee import *
from app import db


class Case(db.Model):
    name = CharField()
    reception = TextField()
    inspection = TextField()
    result = TextField()
    treatment = TextField()
