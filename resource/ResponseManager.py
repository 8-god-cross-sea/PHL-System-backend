import json

from flask import Response


def make_status_response(status_message, status_code, http_response_code=200):
    res = {'status': status_message, 'ret_code': status_code}
    return Response(json.dumps(res), mimetype='application/json', status=http_response_code)
