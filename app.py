from flask import Flask
app = Flask(__name__)
app.config.from_json('config.json')

from resource.UserResource import *


if __name__ == '__main__':
    app.run(debug=True)
