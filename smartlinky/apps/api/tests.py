from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson as json

from apps.core.tests import create_sample_documentation, create_sample_page, create_sample_section, create_sample_link, \
    SAMPLE_DOCUMENTATIONS, SAMPLE_PAGES, SAMPLE_SECTIONS, SAMPLE_LINKS


class APITest(TestCase):
    
    def setUp(self):
        self.page1 = create_sample_page(**SAMPLE_PAGES['pythondocs_builtins'])
        self.page2 = create_sample_page(**SAMPLE_PAGES['pythondocs_intro'])
        self.section1 = create_sample_section(self.page1, **SAMPLE_SECTIONS['pythondocs_builtins_built-in-functions'])
        self.section2 = create_sample_section(self.page1, **SAMPLE_SECTIONS['pythondocs_builtins_non-essential-built-in-functions'])
        self.link1 = create_sample_link(self.section1, **SAMPLE_LINKS['link1'])
        self.link2 = create_sample_link(self.section1, **SAMPLE_LINKS['link2'])
        self.link3 = create_sample_link(self.section2, **SAMPLE_LINKS['link3'])
    
    def get(self, data={}, *args, **kwargs):
        return self.client.get(self.path, data, *args, **kwargs)

    def post(self, data, *args, **kwargs):
        return self.client.post(self.path, data, *args, **kwargs)
    
class InitAPITest(APITest):
    
    def setUp(self):
        self.path = reverse('api_init')
        super(InitAPITest, self).setUp()
        
    def testUnknownUrl(self):
        kwargs = {'url': 'http://google.com'}
        response = self.get(kwargs)
        self.assertEqual(response.content, json.dumps({'sections':{}}))
                         
    def testNoLinks(self):
        kwargs = {'url': self.page2.url}
        response = self.get(kwargs)
        self.assertEqual(response.content, json.dumps({'sections':{}}))
        
    def testSectionsWithLinks(self):
        kwargs = {'url': self.page1.url}
        response = self.get(kwargs)
        self.assertEqual(response.content, json.dumps({
            'sections':{
                self.section1.html_id: self.section1.links.count(), 
                self.section2.html_id: self.section2.links.count(),
            },
        }))
        
#class UserLinksAPITest(APITest):
#    pass
#
#class QALinksAPITest(APITest):
#    pass