from flask_script import Manager
from models import *
from app import app

manager = Manager(app)


@manager.command
def init_db():
    db.connect()

    # create tables
    db.drop_tables(models)
    db.create_tables(models)

    # initialize data
    admin = User.create(username='admin', password='admin')
    admin.save()

    db.close()


if __name__ == "__main__":
    manager.run()
