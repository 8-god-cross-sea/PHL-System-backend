import json

from flask import Response


def make_status_response(status_message, status_code, http_response_code=200):
    res = {'status': status_message, 'ret_code': status_code}
    return Response(json.dumps(res), mimetype='application/json', status=http_response_code)


NOT_PERMITTED_RESPONSE = make_status_response('Not permitted', 101, 403)
LOGIN_SUCCESS_RESPONSE = make_status_response('login success', 0, 200)
LOGIN_FAILED_RESPONSE = make_status_response('incorrect username or password', 101, 202)
LOGOUT_SUCCESS_RESPONSE = make_status_response('You are now logged out', 0, 200)
UPDATED_SUCCESS_RESPONSE = make_status_response('updated', 0)
ALREADY_TAKEN_EXAM_RESPONSE = make_status_response('You have taken this exam', 101, 202)
