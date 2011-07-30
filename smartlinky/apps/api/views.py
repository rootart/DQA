from django.utils import simplejson as json
from django.http import HttpResponse


def demo_init(request):
    init = {
        'sections': {
            's-queryset-api-reference': 3,
            's-when-querysets-are-evaluated': 5,
            's-pickling-querysets': 2
        }
    }
    
    content = json.dumps(init)
    response = HttpResponse(content, mimetype='application/json')
    response['Access-Control-Allow-Origin']  = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE' 
    return response


def demo_user_links(request):
    links = {
        'links': [
            {
                'id': 12,
                'url': 'http://test.com',
                'title': 'Title',
                'is_relevant': True,
                'up_votes': 5,
            },
            {
                'id': 17,
                'url': 'http://example.com',
                'title': 'Example',
                'is_relevant': True,
                'up_votes': 2,
            },
            {
                'id': 14,
                'url': 'http://super.com',
                'title': 'Super',
                'is_relevant': False,
                'up_votes': 2,
            },

        ]
    }
    
    content = json.dumps(links)
    response = HttpResponse(content, mimetype='application/json')
    response['Access-Control-Allow-Origin']  = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE' 
    return response

def demo_qa_links(request):
    links = {
        'links': [
            {
                'url': 'http://test.com',
                'title': 'Title',
            },
            {
                'url': 'http://example.com',
                'title': 'Example',
            },
            {
                'url': 'http://super.com',
                'title': 'Super',
            },

        ]
    }
    
    content = json.dumps(links)
    response = HttpResponse(content, mimetype='application/json')
    response['Access-Control-Allow-Origin']  = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE' 
    return response
