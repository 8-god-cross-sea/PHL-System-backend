from peewee import *
from app import db
from app.model.patient import Patient


class Assay(db.Model):
    patient = ForeignKeyField(Patient)
    description = CharField()
