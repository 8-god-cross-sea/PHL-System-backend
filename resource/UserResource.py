from flask.views import MethodView
from flask import jsonify
from app import app
from models import User
from playhouse.shortcuts import model_to_dict


class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            # return a list of users
            return jsonify([model_to_dict(user) for user in User.select()])
        else:
            # expose a single user
            return jsonify(User.get_by_id(user_id))

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass


def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])


register_api(UserAPI, 'user_api', '/users/', pk='user_id')
