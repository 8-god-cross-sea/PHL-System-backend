from peewee import *

# db = MySQLDatabase(**app.config['DATABASE'])
db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = UUIDField(unique=True)
    username = CharField(unique=True)
    password = CharField()


models = [cls for cls in BaseModel.__subclasses__()]

if __name__ == '__main__':
    from playhouse.shortcuts import model_to_dict

    for user in User.select():
        print(model_to_dict(user))
