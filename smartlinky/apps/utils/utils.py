from datetime import datetime
import BeautifulSoup
import urllib

from django.conf import settings


def get_page_title(url):
    """Return a page's title

    :param url: URL of the page
    :type url: str

    :returns: str

    .. note:: the function does not handle any exception. The caller should take care of them.
    """
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))
    return soup.title.string

# TODO: tests
# TODO: docs
def check_req_lim(request, req_lim_key):
    last = request.session.get(req_lim_key)
    if last:
        delta = datetime.now() - last
        if delta.seconds < settings.REQUESTS_RATE_LIMIT:
            error_message = "Requests rate limit exceeded. Try again in %s seconds." % delta.seconds
            raise Exception(error_message)

# TODO: tests
# TODO: docs
def update_req_lim(request, req_lim_key):
    request.session[req_lim_key] = datetime.now()