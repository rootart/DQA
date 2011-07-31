# TODO: clean this mess up
import re
import urllib2, urllib

from django.conf import settings
from django.utils import simplejson as json
from django.utils.encoding import smart_str

import stackexchange


SO = stackexchange.StackOverflow()

def remove_html_tags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

# TODO: add comments and credits according to http://stackapps.com/questions/198/py-stackexchange-an-api-wrapper-for-python
# TODO: docstrings
# TODO: tests
# TODO: limit the number of results via API
def get_links_via_API(search_query):
    search_results = SO.search(intitle=smart_str(search_query), pagesize=5).items
    links = [{'url': sr.url, 'title': remove_html_tags(sr.title)} for sr in search_results]
    return links

# TODO: docstrings
# TODO: tests
# TODO: limit the number of results via API
def get_links_via_google(search_query, site='stackoverflow.com'):
    if site:
        search_query += ' site=stackoverflow.com'
    get_params = urllib.urlencode({'q': smart_str(search_query)})
    url = 'https://ajax.googleapis.com/ajax/services/search/web?v=1.0&key=%s&%s' % (settings.GOOGLE_API_KEY, get_params)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    search_results = json.load(response)['responseData']['results']
    links = [{'url': sr['url'], 'title': remove_html_tags(sr['title'])} for sr in search_results]
    return links

# TODO: docstrings
# TODO: tests
def get_links(page_title, section_title):
    """Switch between querying StackOverflow via it's API or via Google."""
    # HACK: until we figure out how to query more precisely then google might give more results
    _get_links = get_links_via_google if settings.STACKOVERFLOW_VIA_GOOGLE else get_links_via_API
    
    # most precise search
    links = _get_links('%s %s' % (page_title, section_title))[:settings.QA_LINKS_COUNT]
    
    need_more = len(links) - settings.QA_LINKS_COUNT
    if need_more > 0 :
        # only section_title
        links.extend(_get_links(section_title)[:need_more])
    else:
        return links 

    need_more = len(links) - settings.QA_LINKS_COUNT
    if need_more > 0 :
        # only page_title
        links.extend(_get_links(page_title)[:need_more])
    else:
        return links
        
    need_more = len(links) - settings.QA_LINKS_COUNT
    if need_more > 0 :
        # via google without http://stackoverflow.com site
        links.extend(get_links_via_google('%s %s' % (page_title, section_title), site=None)[:need_more])

    return links