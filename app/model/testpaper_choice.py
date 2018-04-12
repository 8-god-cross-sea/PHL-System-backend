from peewee import *
from app import db
from app.model.choice import Choice
from app.model.test_paper import TestPaper


class TestPaperChoice(db.Model):
    test_paper_id = ForeignKeyField(TestPaper)
    choice_id = ForeignKeyField(Choice)
