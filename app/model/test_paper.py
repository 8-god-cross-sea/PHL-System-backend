from peewee import *
from app import db


class TestPaper(db.Model):
    name = CharField()
