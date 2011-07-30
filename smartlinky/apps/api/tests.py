from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson as json

from apps.core.tests import create_sample_documentation, create_sample_page, create_sample_section, create_sample_link, \
    SAMPLE_DOCUMENTATIONS, SAMPLE_PAGES, SAMPLE_SECTIONS, SAMPLE_LINKS

from apps.core.models import Link


class APITest(TestCase):
    
    def setUp(self):
        self.page1 = create_sample_page(**SAMPLE_PAGES['pythondocs_builtins'])
        self.page2 = create_sample_page(**SAMPLE_PAGES['pythondocs_intro'])
        self.page3 = create_sample_page(**SAMPLE_PAGES['pythondocs_logging'])
        self.section1 = create_sample_section(self.page1, **SAMPLE_SECTIONS['pythondocs_builtins_built-in-functions'])
        self.section2 = create_sample_section(self.page1, **SAMPLE_SECTIONS['pythondocs_builtins_non-essential-built-in-functions'])
        self.section3 = create_sample_section(self.page3, **SAMPLE_SECTIONS['pythondocs_logging_configuration_functions'])
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
                         
    def testPageWithoutLinks(self):
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
        
class UsersLinksAPITest(APITest):
    
    def setUp(self):
        self.path = reverse('api_users_links')
        super(UsersLinksAPITest, self).setUp()
        
    def testUnknownUrl(self):
        kwargs = {
            'url': 'http://google.com',
            'section_id': 'foo',
        }
        response = self.get(kwargs)
        self.assertEqual(response.content, json.dumps({'links':[]}))
                         
    def testUnknownSection(self):
        kwargs = {
            'url': self.page2.url,
            'section_id': 'foo',
        }
        response = self.get(kwargs)
        self.assertEqual(response.content, json.dumps({'links':[]}))
        
    def testSectionWithoutLinks(self):
        kwargs = {
            'url': self.section3.page.url,
            'section_id': self.section3.html_id,
        }
        response = self.get(kwargs)
        self.assertEqual(response.content, json.dumps({'links':[]}))
    
    def testSectionWithLinks(self):
        kwargs = {
            'url': self.section2.page.url,
            'section_id': self.section2.html_id,
        }
        response = self.get(kwargs)
        links = []
        for link in self.section2.links.all():
            links.append({
                'id': link.id,
                'url': link.url,
                'title': link.title,
                'is_relevant': link.is_relevant,
                'up_votes': link.up_votes,
            })
        self.assertEqual(response.content, json.dumps({
            'links': links
        }))
           
#class UserLinksAPITest(APITest):
#    pass
#
#class QALinksAPITest(APITest):
#    pass

class AddLinkAPITest(APITest):
    def setUp(self):
        self.path = reverse('api_add_link')
        super(AddLinkAPITest, self).setUp()

    def testWrongUrl(self):
        Link.objects.all().delete()
        kwargs = {
            'link_url': 'BAD',
            'url': 'http://www.wabidesign.it',
            'page_title': 'Test',
            'section_id': 'test',
            'section_title': 'Test htm',
        }
        response = self.post(kwargs)
        content_json = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual('message' in content_json, True)
        self.assertEqual(Link.objects.all().count(), 0)

    def testMissingArguments(self):
        kwargs = {
            'link_url': 'http://www.wabidesign.it/',
            'url': 'http://example.com',
            'section_id': 'test',
            'section_title': 'Test htm',
        }
        response = self.post(kwargs)
        self.assertEqual(response.status_code, 400)
    
        kwargs = {
            'link_url': 'http://www.wabidesign.it/',
            'url': 'http://example.com',
            'page_title': 'Test',
            'section_title': 'Test htm',
        }
        response = self.post(kwargs)
        self.assertEqual(response.status_code, 400)

        kwargs = {
            'link_url': 'http://www.wabidesign.it/',
            'url': 'http://example.com',
            'page_title': 'Test',
            'section_id': 'test',
        }
        response = self.post(kwargs)
        self.assertEqual(response.status_code, 400)

    def testSimpleUrl(self):
        Link.objects.all().delete()
        kwargs = {
            'link_url': 'http://www.wabidesign.it/',
            'url': 'http://example.com',
            'page_title': 'Test',
            'section_id': 'test',
            'section_title': 'Test htm',
        }
        response = self.post(kwargs)
        content_json = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Antonella Tezza' in content_json['title'], True)
        self.assertEqual(Link.objects.all().count(), 1)


    def testMoreUrls(self):
        Link.objects.all().delete()
        kwargs = {
            'link_url': 'http://virtuallight.pl/',
            'url': 'http://example.com',
            'page_title': 'Test',
            'section_id': 'test',
            'section_title': 'Test htm',
        }
        response = self.post(kwargs)
        content_json = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('things' in content_json['title'], True)
        kwargs = {
            'link_url': 'http://attila.maczak.hu/',
            'url': 'http://example.com',
            'page_title': 'Test',
            'section_id': 'test',
            'section_title': 'Test htm',
        }
        response = self.post(kwargs)
        content_json = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Attila' in content_json['title'], True)

        self.assertEqual(Link.objects.all().count(), 2)

