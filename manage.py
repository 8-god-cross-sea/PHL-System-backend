from flask_script import Manager
from app import app
from app.model import *
from peewee import fn
import json
from os.path import dirname, join

manager = Manager(app)


@manager.command
def init_db():
    """initialize database and create schema"""
    from app import db

    # drop and create tables
    models = db.Model.__subclasses__()
    models += {m2m.get_through_model() for model in models for m2m in model._meta.manytomany.values()}
    model_dict = {model.__name__: model for model in models}

    db.database.drop_tables(models)
    db.database.create_tables(models)

    # initialize data
    from flask_peewee.utils import make_password
    User.create(username='admin', password=make_password('admin'), email='admin@admin.com',
                permission=0b10000)
    user = User.create(username='user', password=make_password('user'), email='user@user.com')
    User.create(username='user2', password=make_password('user2'), email='user2@user.com')

    with open(join(dirname(__file__), 'data.json'), encoding='utf-8') as f:
        data = json.load(f)

    for key, items in data.items():
        model = model_dict[key]
        for item in items:
            model.create(**item)

    TestPaper.get_by_id(1).choices.add(Choice.select().order_by(fn.Random()).limit(3))
    TestPaper.get_by_id(2).choices.add(Choice.select().order_by(fn.Random()).limit(3))

    Exam.get_by_id(1).users.add(User.select().where(User.id > 0))
    Exam.get_by_id(2).users.add(User.select().where(User.id > 1))

    Report.create(user=user, exam=Exam.get_by_id(1), score=100)
    print('db init finished')


if __name__ == '__main__':
    manager.run()
