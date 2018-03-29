from peewee import *
from app import db


class Vaccine(db.Model):
    name = CharField()
    price = DoubleField()
    count = IntegerField()
