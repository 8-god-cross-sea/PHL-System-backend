from peewee import *
from app import db


class CaseType(db.Model):
    name = CharField()
