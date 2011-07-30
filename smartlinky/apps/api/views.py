from decorators import xss_json_response

# TODO: remove when proper api views are working
from views_demo import demo_init, demo_user_links, demo_qa_links

 
# TODO: add tests
# TODO: add sample response to docstring
@xss_json_response
def init(request):
    """Return number of user links for known sections of a documentation page.
    
    :param url: url of the documentation page
    :type url: str
    
    :returns:  dict

    .. note:: xss_json_response decorator dumps the response into a json, wraps with a HttpResponse
        and makes it xss friendly
    """
    # page
    url = request.GET['url']
    return content

# TODO: add tests
# TODO: add sample response to docstring
@xss_json_response
def user_links(request):
    """Return all user links for a given section.
    
    :param url: url of the documentation page containing the section
    :type url: str
    
    :param id: id of the html tag containing the section
    :type id: str

    :returns:  dict

    .. note:: xss_json_response decorator dumps the response into a json, wraps with a HttpResponse
        and makes it xss friendly
    """
    # page
    url = request.GET['url']
    # section
    html_id = request.GET['id']
    return content
             
# TODO: add tests
# TODO: add sample response to docstring
@xss_json_response
def qa_links(request):
    """Return a set of QA links for a given section.
    
    :param url: url of the documentation page containing the section
    :type url: str
    
    :param page_title: meta title of the documentation page containing the section
    :type page_title: str
    
    :param id: id of the html tag containing the section
    :type id: str
    
    :param section_title: title of section
    :type section_title: str

    :returns:  dict

    .. note:: xss_json_response decorator dumps the response into a json, wraps with a HttpResponse
        and makes it xss friendly
    """
    # page
    url = request.GET['url']
    meta_title = request.GET['page_title']
    # section
    html_id = request.GET['id']
    html_title = request.GET['section_title']
    return content