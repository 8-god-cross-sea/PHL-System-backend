from flask import Flask


def init():
    global app
    app = Flask(__name__)
    app.config.from_json('config.json')
