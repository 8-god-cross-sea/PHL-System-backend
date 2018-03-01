from peewee import *
from app import app


db = MySQLDatabase(**app.config['DATABASE'])


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


models = [cls for cls in BaseModel.__subclasses__()]
