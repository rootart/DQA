from django.utils import unittest
from models import Documentation, Page, Section, Link


def _create_sample_documentation(**kwargs):
    """Create a sample Documentation object."""
    documentation = Documentation.objects.create(**kwargs)
    return documentation

def _create_sample_page(documentation=None, **kwargs):
    """Create a sample Page object."""
    page = Page.objects.create(documentation=documentation, **kwargs)
    return page

def _create_sample_section(page,**kwargs):
    """Create a sample Section object."""
    section = Section.objects.create(page=page, **kwargs)
    return section

def _create_sample_link(section, **kwargs):
    """Create a sample Link object."""
    link = Link.objects.create(section=section, **kwargs)
    return link

SAMPLE_DOCUMENTATIONS = {
    'djangodocs': {
        'url': 'https://docs.djangoproject.com/en/1.3/',
        'title': 'Django 1.3 documentation',
    },
    'pythondocs': {
        'url': 'http://docs.python.org/library/',
        'title': 'Python 2.7 documentation',
    },
}    

SAMPLE_PAGES = {
    'pythondocs_intro': {
        'url': 'http://docs.python.org/library/intro.html',
    },
    'pythondocs_builtins': {
        'url': 'http://docs.python.org/library/functions.html',
    },
}

SAMPLE_SECTIONS = {
    'pythondocs_builtins_built-in-functions': {
        'html_id': 'built-in-functions',
        'html_title': '2. Built-in Functions',
    },
    'pythondocs_builtins_non-essential-built-in-functions': {
        'html_id': 'non-essential-built-in-functions',
        'html_title': '3. Non-essential Built-in Functions',
    },
}

SAMPLE_LINKS = {
    'link1': {
        'url': 'http://www.joelonsoftware.com/articles/fog0000000069.html',
        'title': 'Things You Should Never Do, Part I',
    },
    'link2': {
        'url': 'http://rhettinger.wordpress.com/2011/01/28/open-your-source-more/',
        'title': 'Open Source Challenge: Open Your Source, More',
    },
}


class DocumentationTestCase(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def testCreation(self):
        """Test if documentations are created properly."""
        djangodocs = _create_sample_documentation(**SAMPLE_DOCUMENTATIONS['djangodocs'])
        self.assertNotEqual(djangodocs, None)
        pythondocs = _create_sample_documentation(**SAMPLE_DOCUMENTATIONS['pythondocs'])
        self.assertNotEqual(pythondocs, None)
        
class PageTestCase(unittest.TestCase):
    
    def setUp(self):
        self.documentation = _create_sample_documentation(**SAMPLE_DOCUMENTATIONS['pythondocs'])
     
    def testCreation(self):
        """Test if pages are created properly."""
        pythondocs_intro = _create_sample_page(self.documentation, **SAMPLE_PAGES['pythondocs_intro'])
        self.assertNotEqual(pythondocs_intro, None)   
        pythondocs_builtins = _create_sample_page(**SAMPLE_PAGES['pythondocs_builtins'])
        self.assertNotEqual(pythondocs_builtins, None) 

class SectionTestCase(unittest.TestCase):
    
    def setUp(self):
        self.documentation = _create_sample_documentation(**SAMPLE_DOCUMENTATIONS['pythondocs'])
        self.page = _create_sample_page(self.documentation, **SAMPLE_PAGES['pythondocs_builtins'])
     
    def testCreation(self):
        """Test if sections are created properly."""
        pythondocs_builtins_built_in_functions = _create_sample_section(self.page, **SAMPLE_SECTIONS['pythondocs_builtins_built-in-functions'])
        self.assertNotEqual(pythondocs_builtins_built_in_functions, None)   
        pythondocs_builtins_non_essential_built_in_functions = _create_sample_section(self.page, **SAMPLE_SECTIONS['pythondocs_builtins_non-essential-built-in-functions'])
        self.assertNotEqual(pythondocs_builtins_non_essential_built_in_functions, None)

class LinkTestCase(unittest.TestCase):
    
    def setUp(self):
        self.documentation = _create_sample_documentation(**SAMPLE_DOCUMENTATIONS['pythondocs'])
        self.page = _create_sample_page(self.documentation, **SAMPLE_PAGES['pythondocs_builtins'])
        self.section = _create_sample_section(self.page, **SAMPLE_SECTIONS['pythondocs_builtins_built-in-functions'])
        self.link = _create_sample_link(self.section, **SAMPLE_LINKS['link1']) # not really about this section...
        
    def testIncrUpVotes(self):
        """Test 'incr_up_votes' method of Link."""
        up_votes = self.link.up_votes
        self.link.incr_up_votes()
        self.assertEquals(up_votes + 1, self.link.up_votes)
        
    def testIncrClicks(self):
        """Test 'incr_clicks' method of Link."""
        clicks = self.link.clicks
        self.link.incr_clicks()
        self.assertEquals(clicks + 1, self.link.clicks)
        
    def testSetRelevant(self):
        """Test 'set_relevant' method of Link."""
        self.link.set_relevant(False)
        self.assertEquals(self.link.is_relevant, False)
        self.link.set_relevant()
        self.assertEquals(self.link.is_relevant, True)