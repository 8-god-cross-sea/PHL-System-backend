from peewee import *
from app import db
from app.model.choice import Choice


class TestPaper(db.Model):
    name = CharField()

    choices = ManyToManyField(Choice, backref='testpapers')
