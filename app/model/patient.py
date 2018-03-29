from peewee import *
from app import db


class Patient(db.Model):
    name = CharField()
    description = CharField()
