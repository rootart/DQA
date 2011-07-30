# TODO: remove when proper api views are working

from decorators import xss_json_response


@xss_json_response
def demo_init(request):
    return {
        'sections': {
            's-queryset-api-reference': 3,
            's-when-querysets-are-evaluated': 5,
            's-pickling-querysets': 2
        }
    }
    
@xss_json_response
def demo_user_links(request):
    return {
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
    return links

@xss_json_response
def demo_qa_links(request):
    return  {
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