from peewee import *
from app import db
from app.model.user import User
from app.model.exam import Exam


class Report(db.Model):
    user = ForeignKeyField(User)
    exam = ForeignKeyField(Exam)
    score = DoubleField()
