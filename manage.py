from flask_script import Manager
from app import app

manager = Manager(app)


@manager.command
def init_db():
    """initialize database and create schema"""
    from app import db
    db.database.connect()

    # drop and create tables
    from app.model.user import User
    tables = [User]
    db.database.drop_tables(tables)
    db.database.create_tables(tables)

    # initialize data
    from flask_peewee.utils import make_password
    User.create(username='admin', password=make_password('admin'), email='admin@admin.com', permission=int('10000', 2))
    User.create(username='user', password=make_password('user'), email='user@user.com')
    User.create(username='user2', password=make_password('user2'), email='user2@user.com')

    db.database.close()


if __name__ == '__main__':
    manager.run()
