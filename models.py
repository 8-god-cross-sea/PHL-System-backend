from peewee import *
from playhouse.db_url import connect
import settings

app = settings.app
db = connect(app.config['DATABASE_URI'])


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = UUIDField(unique=True)
    username = CharField(unique=True)
    password = CharField()


tables = [cls for cls in BaseModel.__subclasses__()]

if __name__ == '__main__':
    from playhouse.shortcuts import model_to_dict

    for user in User.select():
        print(model_to_dict(user))
