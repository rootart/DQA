# TODO: clean this mess up
import urllib2, urllib

from django.conf import settings
from django.utils import simplejson as json
from django.utils.encoding import smart_str

import stackexchange


SO = stackexchange.StackOverflow()

# TODO: add comments and credits according to http://stackapps.com/questions/198/py-stackexchange-an-api-wrapper-for-python
# TODO: add tests
def get_links_via_API(page_title, section_title):
    search_query = '%s %s' % (page_title, section_title)
    search_results = SO.search(intitle=smart_str(search_query), pagesize=5).items
    links = [{'url': sr.url, 'title': sr.title} for sr in search_results]
    return links[:settings.QA_LINKS_COUNT]

# TODO: add docstrings
# TODO: add tests
def get_links_via_google(page_title, section_title):
    search_query = '%s %s' % (page_title, section_title)
    url = 'https://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s%s' % (urllib.urlencode({'q': smart_str(search_query)}), urllib.urlencode({'site': 'stackoverflow.com'}))
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    search_results = json.load(response)['responseData']['results']
    links = [{'url': sr['url'], 'title': sr['title']} for sr in search_results]
    return links[:settings.QA_LINKS_COUNT]
    
def get_links(page_title, section_title):
    """Switch between querying StackOverflow via it's API or via Google."""
    _get_links = get_links_via_google if settings.STACKOVERFLOW_VIA_GOOGLE else get_links_via_API
    links = _get_links(page_title, section_title)
    if not links:
        links = _get_links('', section_title)
    if not links:
        links = _get_links(page_title, '')
    return links     