from peewee import *
from app import db
from app.model.test_paper import TestPaper


class Exam(db.Model):
    test_paper_id = ForeignKeyField(TestPaper)
    name = CharField()
    duration = DoubleField()
    start = DateTimeField()
