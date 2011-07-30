from functools import wraps

from django.http import HttpResponse
from django.utils import simplejson as json


def xss_json_response(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        content = f(*args, **kwargs)
        response = HttpResponse(json.dumps(content), mimetype='application/json')
        response['Access-Control-Allow-Origin']  = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE' 
        return response
    return wrapper
