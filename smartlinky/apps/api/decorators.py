from functools import wraps
from pprint import pprint
import logging

from django.http import HttpResponse, HttpResponseBadRequest
from django.utils import simplejson as json


logger = logging.getLogger(__name__)

def xss_json_response(f):
    """Dump a function result into a json, wrap with HttpResponse and make xss friendly."""
    
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            content = f(*args, **kwargs)
        except Exception, e:
            logger.error('{%s@xss_json_response} %s' % (f.__name__, pprint(e)))
            content = {'message': pprint(e)}
            response = HttpResponseBadRequest(json.dumps(content), mimetype='application/json')
        else:    
            response = HttpResponse(json.dumps(content), mimetype='application/json')
        finally:
            response['Access-Control-Allow-Origin']  = '*'
            response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE' 
            return response
    return wrapper
