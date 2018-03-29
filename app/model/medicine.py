from peewee import *
from app import db


class Medicine(db.Model):
    name = CharField()
    price = DoubleField()
    count = DoubleField()