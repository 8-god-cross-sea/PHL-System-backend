from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_json('../config.json')
cors = CORS(app)
