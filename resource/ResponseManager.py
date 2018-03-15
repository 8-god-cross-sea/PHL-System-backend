from flask import Response
import json


def make_status_response(status, status_code):
    res = {'status': status, 'ret_code': status_code}
    return Response(json.dumps(res), mimetype='application/json')
