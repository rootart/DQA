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
    return HttpResponse(content, mimetype='application/json')


def demo_get_section(request):
    pass
