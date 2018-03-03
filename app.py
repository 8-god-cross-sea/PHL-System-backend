import settings

settings.init()
from resource.UserResource import *

if __name__ == '__main__':
    settings.app.run(debug=True)
