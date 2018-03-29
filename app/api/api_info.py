import json
import os

from flask import Response
from flask import redirect, url_for
from flask import request

from app.api.api_rest_resource import APIRestResource


def api_info(app):
    @app.route('/')
    def redirect_root():
        return redirect(url_for('api_overview'))

    @app.route('/api')
    def api_overview():
        api_url_mapping = {}
        url = request.base_url
        for api in APIRestResource.__subclasses__():
            model_name = api.get_model().__name__.lower()
            api_url_mapping[model_name + '_url'] = url + '/' + model_name
        api_url_mapping['BUILD_INFO'] = '{0} {1}'.format(os.getenv('HEROKU_RELEASE_VERSION'),
                                                         os.getenv('HEROKU_RELEASE_CREATED_AT'))
        return Response(json.dumps(api_url_mapping), mimetype='application/json', status=200)
