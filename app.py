from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_json('config.json')

db = Database(app)
