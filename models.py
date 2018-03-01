from peewee import *

# db = MySQLDatabase(**app.config['DATABASE'])
db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


models = [cls for cls in BaseModel.__subclasses__()]
