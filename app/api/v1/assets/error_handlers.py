import json
from flask import Response
from app import app
from .response import CODES, MESSAGES, MIME_TYPES


# custom base 404 error handler
# noinspection PyUnusedLocal
@app.errorhandler(CODES.get('NOT_FOUND'))
def not_found(error):
    data = {
        'message': MESSAGES.get('RESOURCE_NOT_FOUND'),
        'status_code': CODES.get('RESOURCE_NOT_FOUND')
    }

    response = Response(json.dumps(data), status=CODES.get('NOT_FOUND'),
                        mimetype=MIME_TYPES.get('APPLICATION_JSON'))
    return response


@app.errorhandler(CODES.get('METHOD_NOT_ALLOWED'))
def method_not_allowed(error):
    data = {
        "message":MESSAGES.get('METHOD_NOT_ALLOWED'),
        "status_code": CODES.get('METHOD_NOT_ALLOWED')
    }

    response = Response(json.dumps(data), status=CODES.get('METHOD_NOT_ALLOWED'),
                        mimetype=MIME_TYPES.get('APPLICATION_JSON'))
    return response


def custom_response(message, status, mimetype):
    data = {
        "message": message,
        "status_code": status,
    }

    response = Response(json.dumps(data), status=status, mimetype=mimetype)
    return response
