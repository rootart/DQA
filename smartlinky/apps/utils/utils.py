import urllib
import BeautifulSoup

def get_page_title(url):
    """Return a page's title

    :param url: URL of the page
    :type url: str

    :returns: str

    .. note:: the function does not handle any exception. The caller should take care of them.
    """
    soup = BeautifulSoup.BeautifulSoup(urllib.urlopen(url))
    return soup.title.string
