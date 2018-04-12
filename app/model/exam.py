from peewee import *
from app import db
from app.model.testpaper import TestPaper
from app.model.user import User


class Exam(db.Model):
    test_paper = ForeignKeyField(TestPaper)
    name = CharField()
    duration = DoubleField()
    start = DateTimeField()

    users = ManyToManyField(User, backref='exams')
