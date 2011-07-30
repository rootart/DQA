import logging

from django.conf import settings
from django.db import models


logger = logging.getLogger(__name__)

# TODO: add db indexes
# TODO: add help text
# TODO: add managment command to remove all irrelevant links
class Documentation(models.Model):
    """Documentation is grouping pages according to the product that they document, 
    usually in one of it's versions (e.g. https://docs.djangoproject.com/en/1.3/)."""
    
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)

    meta_title = models.TextField(default='', blank=True) # used to refine searches agains QAs APIs, extracted from site's head
    meta_keywords = models.TextField(default='', blank=True) # used to refine searches agains QAs APIs, extracted from site's head
    meta_description = models.TextField(default='', blank=True) # used to refine searches agains QAs APIs, extracted from site's head

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    # TODO: add tests
    def delete_irrelevant_links(self, older_than=None, by_create_date=True, by_mod_date=False):
        """Clean up irrelevant links for all sections of all pages of this documentation.
        Delete links with creation or modification date older than a given date.
        
        .. warning:: Cleans up ALL links if 'older_than' is not specified."""
        pages = self.pages
        for page in self.pages:
            page.delete_irrelevant_links(older_than, by_create_date, by_mod_date)
        
    # TODO: implement using fetch_meta from utils
    # TODO: add tests
    def fetch_meta(self):
        """Fetch the documentation's meta-related information (html meta)
        and update corresponding fields."""
        raise NotImplementedError 
        
                                
# TODO: add db indexes
# TODO: add help text
# TODO: add managment command to remove all irrelevant links
class Page(models.Model):
    """Page represents one url (one page) of the documentation."""

    url = models.URLField()
    documentation = models.ForeignKey(Documentation, related_name='pages', null=True, blank=True)

    meta_title = models.TextField(default='', blank=True) # used to refine searches agains QAs APIs, extracted from site's head
    meta_keywords = models.TextField(default='', blank=True) # used to refine searches agains QAs APIs, extracted from site's head
    meta_description = models.TextField(default='', blank=True) # used to refine searches agains QAs APIs, extracted from site's head
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    # TODO: add tests
    def delete_irrelevant_links(self, older_than=None, by_create_date =True, by_mod_date=False):
        """Clean up irrelevant links for all sections of the page.
        Delete links with creation or modification date older than a given date.
        
        .. warning:: Cleans up ALL links if 'older_than' is not specified."""
        sections = self.sections
        for section in self.sections:
            section.delete_irrelevant_links(older_than, by_create_date, by_mod_date)
        
    # TODO: implement using fetch_meta from utils
    # TODO: add tests
    def fetch_meta(self):
        """Fetch the page's meta-related information (html meta) 
        and update corresponding fields."""
        raise NotImplementedError     


# TODO: add db indexes
# TODO: add help text
# TODO: add objects managers or properties to retrieve specific links (irrelevant, relevant or all)
class Section(models.Model):
    """Section is a section of the documentation's page which is specific enough 
    to attach links to it."""

    html_id = models.CharField(max_length=100)
    html_title = models.CharField(max_length=100)
    page = models.ForeignKey(Page, related_name='sections')
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    # TODO: add tests
    def delete_irrelevant_links(self, older_than=None, by_create_date =True, by_mod_date=False):
        """Clean up irrelevant links of the section.
        Delete links with creation or modification date older than a given date.
        
        .. warning:: Cleans up ALL links if 'older_than' is not specified."""
        # TODO: check if this works
        self.sections.delete()


# TODO: add db indexes
# TODO: add help text
# TODO: add uniqueness within a section according to url
class Link(models.Model):
    """Link is a connection between an link and a section.
    
    Links are url-unique within a section."""

    url = models.URLField()
    title = models.CharField(max_length=100) # 40 char field, obligatory, default is the meta title of the linked site, serves also as a description
    section = models.ForeignKey(Section, related_name='links')
    
    is_relevant = models.BooleanField(default=True)
    up_votes = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)

    validated_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False) # does auto_now_add set editable to False automatically?
    
    # TODO: faster increment by counter type fields or raw sql
    def incr_up_votes(self):
        """Increment 'up_votes' by 1."""
        self.up_votes += 1
    
    # TODO: faster increment by counter type fields or raw sql
    def incr_clicks(self):
        """Increment 'clicks' by 1."""
        self.clicks += 1
    
    def set_relevant(self, is_relevant=True):
        """Set 'is_relevant' value to True(deafult) or False."""
        self.is_relevant = is_relevant
    
    # TODO: add tests
    # TODO: add url checking method to docstring
    def validate_url(self):
        """Check if the url is still valid."""
        raise NotImplementedError
    
    # TODO: add tests
    def delete(self, *args, **kwargs):
        """Log the link data before deleting it."""
        logger.info('{link.delete} %s' % self.__dict__)
        super(Link, self).delete(*args, **kwargs)