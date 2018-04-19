from peewee import *
from app import db
from app.model.case_type import CaseType


class Choice(db.Model):
    case_type = ForeignKeyField(CaseType)
    description = CharField()
    choice_a = CharField()
    choice_b = CharField()
    choice_c = CharField(null=True)
    choice_d = CharField(null=True)
    choice_e = CharField(null=True)
    answer = IntegerField()
