from flask_script import Manager
from app import app
from app.model import *
import datetime

manager = Manager(app)


@manager.command
def init_db():
    """initialize database and create schema"""
    from app import db

    # drop and create tables
    models = db.Model.__subclasses__()
    models += {m2m.get_through_model() for model in models for m2m in model._meta.manytomany.values()}
    db.database.drop_tables(models)
    db.database.create_tables(models)

    # initialize data
    from flask_peewee.utils import make_password
    admin = User.create(username='admin', password=make_password('admin'), email='admin@admin.com',
                        permission=0b10000)
    user = User.create(username='user', password=make_password('user'), email='user@user.com')
    user2 = User.create(username='user2', password=make_password('user2'), email='user2@user.com')
    patient = Patient.create(name='汇汇的哈士奇', description='很2的狗')
    InHospital.create(patient=patient, status='已入院')
    Department.create(name='档案室', description='包括病例档案的合理保存与统计')
    Vaccine.create(name='感冒疫苗', price=150, count=20)
    Assay.create(patient=patient, wbc=9.4, rbc=5.1, plt=300)
    Medicine.create(name='阿司匹林', price=21.3, count=140)
    Role.create(name='前台', description='<b>前台的描述</b>')
    Role.create(name='医助', description='<b>医助的描述</b>')
    Role.create(name='兽医师', description='<b>兽医师的描述</b>')

    Case.create(name='膀胱结石', reception='<b>膀胱结石</b>的基本情况', inspection='<b>膀胱结石</b>检查项目及结果', result='<b>膀胱结石</b>诊断结果',
                treatment='<b>膀胱结石</b>治疗方案')

    case_type1 = CaseType.create(name='病种类别1')
    case_type2 = CaseType.create(name='病种类别2')
    case_type3 = CaseType.create(name='病种类别3')

    c1_1 = Choice.create(case_type=case_type1, description='这题选A', choice_a='选项A', choice_b='选项B', choice_c='选项C',
                         answer=0)
    c1_2 = Choice.create(case_type=case_type1, description='这题选D', choice_a='选项A', choice_b='选项B', choice_c='选项C',
                         choice_d='选项D', answer=3)
    c2_1 = Choice.create(case_type=case_type2, description='这题选B', choice_a='选项A', choice_b='选项B', choice_c='选项C',
                         choice_d='选项D', answer=1)
    c2_2 = Choice.create(case_type=case_type2, description='这题选C', choice_a='选项A', choice_b='选项B', choice_c='选项C',
                         choice_d='选项D', answer=2)
    c3_1 = Choice.create(case_type=case_type3, description='这题选D', choice_a='选项A', choice_b='选项B', choice_c='选项C',
                         choice_d='选项D', answer=3)
    c3_2 = Choice.create(case_type=case_type3, description='这题选A', choice_a='选项A', choice_b='选项B', choice_c='选项C',
                         choice_d='选项D', answer=0)

    tp1 = TestPaper.create(name='试卷1')
    tp2 = TestPaper.create(name='试卷2')

    ex1 = Exam.create(test_paper=tp1, name='第一次考试', duration=60, start=str(datetime.datetime(2018, 4, 15, 12)))
    ex2 = Exam.create(test_paper=tp2, name='第二次考试', duration=60, start=str(datetime.datetime(2018, 4, 16, 12)))

    print('db init finished')


if __name__ == '__main__':
    manager.run()
