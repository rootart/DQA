from django.conf import settings
from django.core.cache import cache
from django.db.models import Count
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from apps.core.models import Page, Section, Link
from apps.utils.qa_backends import stackoverflow
from apps.utils.utils import get_page_title

from decorators import xss_json_response
from forms import AddLinkForm


@xss_json_response
def init(request):
    """Return number of user links for known sections of a documentation page.
    
    GET type request.

    :param url: url of the documentation page
    :type url: str
    
    :returns: dict
    
    :example:
        {
        'sections': {
        's-queryset-api-reference': 3,
        's-when-querysets-are-evaluated': 5,
        's-pickling-querysets': 2
        }
        }

    .. note:: xss_json_response decorator dumps the response into a json, wraps with a HttpResponse
        and makes it xss friendly
    """
    # page
    url = request.GET['url']
    
    response = {'sections': {}}
    try:
        page = Page.objects.get(url=url)
    except Page.DoesNotExist:
        return response
    
    for section in page.sections.annotate(num_links=Count('links')):
        response['sections'][section.html_id] = section.num_links
    
    return response

@xss_json_response
def users_links(request):
    """Return all links added by users for a given section.
    
    GET type request.

    :param url: url of the documentation page containing the section
    :type url: str
    
    :param section_id: id of the html tag containing the section
    :type section_id: str

    :returns: dict

    :example:
        {'links': [{
        'id': 12,
        'url': 'http://test.com',
        'title': 'Title',
        'is_relevant': True,
        'up_votes': 5,}, {
        'id': 17,
        'url': 'http://example.com',
        'title': 'Example',
        'is_relevant': True,
        'up_votes': 2,}, {
        'id': 14,
        'url': 'http://super.com',
        'title': 'Super',
        'is_relevant': False,
        'up_votes': 2,},]}
    

    .. note:: xss_json_response decorator dumps the response into a json, wraps with a HttpResponse
        and makes it xss friendly
    """
    # page
    url = request.GET['url']
    
    # section
    html_id = request.GET['section_id']
    
    response = {'links': []}
    try:
        page = Page.objects.get(url=url)
    except Page.DoesNotExist:
        return response    
    try:
        section = Section.objects.get(page=page, html_id=html_id)
    except Section.DoesNotExist:
        return response
    
    for link in section.links.all():
        response['links'].append({
            'id': link.id,
            'url': link.url,
            'title': link.title,
            'is_relevant': link.is_relevant,
            'up_votes': link.up_votes,
        })
    return response
             
@xss_json_response
def qa_links(request):
    """Return a set of QA links for a given section.
    
    GET type request.
    
    :param url: url of the documentation page containing the section
    :type url: str
    
    :param page_title: meta title of the documentation page containing the section
    :type page_title: str
    
    :param section_id: id of the html tag containing the section
    :type section_id: str
    
    :param section_title: title of section
    :type section_title: str

    :returns:  dict
    
    :example:
        {'links': [{
        'url': 'http://test.com',
        'title': 'Title',}, {
        'url': 'http://example.com',
        'title': 'Example',}, {
        'url': 'http://super.com',
        'title': 'Super',},]}

    .. note:: xss_json_response decorator dumps the response into a json, wraps with a HttpResponse
        and makes it xss friendly
    """
    # page
    url = request.GET['url']
    page_title = request.GET['page_title']
    
    # section
    html_id = request.GET['section_id']
    section_title = request.GET['section_title']

    cache_key = '%s%s' % (url, html_id)
    links = cache.get(cache_key)
    if links == None:
        links = stackoverflow.get_links(page_title, section_title)
        cache.set(cache_key, links, settings.QA_CACHE_TIMEOUT)
        
    # TODO: fill up to 5 with links from google for "page_title Q&A" 
    response = {'links': links}
    return response

# TODO: add error responses to docstring
# TODO: limit calls per ip in time
@require_POST
@csrf_exempt
@xss_json_response
def add_link(request):
    """Create a new link in a given section of a documentation page.
    If the section and page don't exist create them as well.

    POST type request.

    :param page_title: Title of documentation's page
    :type page_title: str

    :param url: URL of documentation's page
    :type url: str

    :param section_id: HTML ID of section
    :type section_id: str

    :param section_title: Title of section
    :type section_title: str

    :param link_url: URL of new link
    :type link_url: str
    
    :returns:  dict
    
    :example:
        {'id': 7,
        'url': 'http://one.to.rule_them.al/l,
        'title': 'Knights of Foo Bar,
        'is_relevant': True,}
    """
    form = AddLinkForm(request.POST)
    if form.is_valid():
        try:
            # Fetch & parse the linked page
            link_title = get_page_title(form.cleaned_data['link_url'])
        except Exception, e:
            # TODO: convert into a custom APIException
            # TODO: better message
            raise Exception('No title')

        page, created = Page.objects.get_or_create(url=form.cleaned_data['url'], defaults={'meta_title': form.cleaned_data['page_title']})
        section, created = Section.objects.get_or_create(html_id=form.cleaned_data['section_id'], page=page, defaults={'html_title': form.cleaned_data['section_title']})
        link, created = Link.objects.get_or_create(url=form.cleaned_data['link_url'], section=section, defaults={'title': link_title})

        response = {
            'id': link.id,
            'url': form.cleaned_data['link_url'],
            'title': link_title,
            'is_relevant': True,
        }
        return response
    # TODO: convert into a custom APIException
    # TODO: better message
    raise Exception('problem!')

# TODO: docs
# TODO: samples
# TODO: tests
# TODO: implement
# TODO: limit calls per ip for a link id in time
@require_POST
@csrf_exempt
@xss_json_response
def vote_up(request):
    """Increment the 'up_votes' count for a link.
    
    POST type request.
    
    :param : id of a link
    :type : int
    
    :returns: dict
    
    :example:
        {}
    """
    link_id = int(request.POST['id'])
    link = get_object_or_404(Link, id=link_id)
    link.incr_vote_up()
    link.save()
    return {}

# TODO: docs
# TODO: samples
# TODO: tests
# TODO: implement
# TODO: limit calls per ip for a link id in time
@require_POST
@csrf_exempt
@xss_json_response
def set_relevant(request):
    """Set the 'is_relevant' flag of a link.
    
    POST type request.
    
    :param : id of a link
    :type : int
    
    :param : is_relevant
    :values : 0 or 1
    :type : int
    
    :returns: dict
    
    :example:
        {}
    """
    link_id = int(request.POST['id'])
    is_relevant = int(request.POST['is_relevant'])
    
    if not is_relevant in [0, 1]:
        # TODO: convert into a custom APIException
        # TODO: better message
        raise Exception('invalid format')
    
    link = get_object_or_404(Link, id=link_id)
    link.set_relevant(bool(is_relevant))
    link.save()
    return {}