from flask import Flask
from flask_cors import CORS
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_json('config.json')
cors = CORS(app)

db = Database(app)
