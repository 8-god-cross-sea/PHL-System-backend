from peewee import *
from app import db
from app.model.exam import Exam
from app.model.user import User


class ExamUser(db.Model):
    exam_id = ForeignKeyField(Exam)
    user_id = ForeignKeyField(User)
