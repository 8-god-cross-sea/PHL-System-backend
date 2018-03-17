from phl_app import app
import api

if __name__ == '__main__':
    api.setup(app)
    app.run(debug=False)

