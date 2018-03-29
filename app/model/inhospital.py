import datetime
from peewee import *
from app import db
from app.model.patient import Patient


class InHospital(db.Model):
    patient = ForeignKeyField(Patient)
    join_date = DateTimeField(default=datetime.datetime.now)
    leave_date = DateTimeField(null=True)
    status = CharField()
