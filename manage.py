from flask_script import Manager
from app import app
from app.model import *

manager = Manager(app)


@manager.command
def init_db():
    """initialize database and create schema"""
    from app import db

    # drop and create tables
    models = db.Model.__subclasses__()
    db.database.drop_tables(models)
    db.database.create_tables(models)

    # initialize data
    from flask_peewee.utils import make_password
    User.create(username='admin', password=make_password('admin'), email='admin@admin.com', permission=int('10000', 2))
    User.create(username='user', password=make_password('user'), email='user@user.com')
    User.create(username='user2', password=make_password('user2'), email='user2@user.com')
    patient = Patient.create(name='汇汇的哈士奇', description='很2的狗')
    InHospital.create(patient=patient, status='已入院')
    Department.create(name='档案室', description='包括病例档案的合理保存与统计')
    Vaccine.create(name='感冒疫苗', price=150, count=20)
    Assay.create(patient=patient, wbc=9.4, rbc=5.1, plt=300)
    Medicine.create(name='阿司匹林', price=21.3, count=140)


if __name__ == '__main__':
    manager.run()
