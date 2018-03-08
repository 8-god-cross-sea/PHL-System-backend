from app import app, db

from auth import *
from api import api
from models import *
from resource import register_resource

api.setup()


if __name__ == '__main__':
    app.run()
