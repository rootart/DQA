import logging

from django.conf import settings
from django.db import models


logger = logging.getLogger('smartlinky')

# TODO: indexes
# TODO: help texts
# TODO: managment command to remove all irrelevant links
# TODO: docstrings for fields
class Documentation(models.Model):
    """Documentation is grouping pages according to the product that they document, 
    usually in one of it's versions (e.g. https://docs.djangoproject.com/en/1.3/)."""
    
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)

    meta_title = models.TextField(default='', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    # TODO: tests
    def delete_irrelevant_links(self, older_than=None, by_create_date=True, by_mod_date=False):
        """Clean up irrelevant links for all sections of all pages of this documentation.
        Delete links with creation or modification date older than a given date.
        
        .. warning:: Cleans up ALL links if 'older_than' is not specified."""
        pages = self.pages
        for page in self.pages:
            page.delete_irrelevant_links(older_than, by_create_date, by_mod_date)
        
    # TODO: tests
    # TODO: implement
    def fetch_meta(self):
        """Fetch the documentation's meta-related information (html meta)
        and update corresponding fields."""
        raise NotImplementedError 
        
                                
# TODO: indexes
# TODO: help texts
# TODO: managment command to remove all irrelevant links
# TODO: docstrings for fields
class Page(models.Model):
    """Page represents one url (one page) of the documentation."""

    url = models.URLField(unique=True)
    documentation = models.ForeignKey(Documentation, related_name='pages', null=True, blank=True)

    meta_title = models.TextField(default='', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    # TODO: tests
    def delete_irrelevant_links(self, older_than=None, by_create_date =True, by_mod_date=False):
        """Clean up irrelevant links for all sections of the page.
        Delete links with creation or modification date older than a given date.
        
        .. warning:: Cleans up ALL links if 'older_than' is not specified."""
        sections = self.sections
        for section in self.sections:
            section.delete_irrelevant_links(older_than, by_create_date, by_mod_date)
        
    # TODO: tests
    # TODO: implement
    def fetch_meta(self):
        """Fetch the page's meta-related information (html meta) 
        and update corresponding fields."""
        raise NotImplementedError     


# TODO: indexes
# TODO: help texts
# TODO: managers for relevant and irrelevant links per section
# TODO: docstrings for fields
class Section(models.Model):
    """Section is a section of the documentation's page which is specific enough 
    to attach links to it."""

    html_id = models.CharField(max_length=100)
    html_title = models.CharField(max_length=100)
    page = models.ForeignKey(Page, related_name='sections')
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        unique_together = (("html_id", "page"),)
        
    # TODO: tests
    # TODO: implement
    def delete_irrelevant_links(self, older_than=None, by_create_date =True, by_mod_date=False):
        """Clean up irrelevant links of the section.
        Delete links with creation or modification date older than a given date.
        
        .. warning:: Cleans up ALL links if 'older_than' is not specified."""
        # TODO: check if this works
        raise NotImplementedError
    
    # TODO: tests
    @property
    def cache_key(self):
        """Generate a cache key based on unique fields.""" 
        return '%s%s' % (self.page.url, self.html_id)

# TODO: indexes
# TODO: help texts
# TODO: docstrings for fields
class Link(models.Model):
    """Link is a connection between an link and a section.
    
    Links are url-unique within a section."""

    url = models.URLField()
    title = models.CharField(max_length=100)
    section = models.ForeignKey(Section, related_name='links')
    
    is_relevant = models.BooleanField(default=True)
    up_votes = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)

    validated_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    class Meta:
        unique_together = (("url", "section"),)

    # TODO: faster increment by counter type fields or raw sql
    def incr_up_votes(self):
        """Increment 'up_votes' by 1."""
        self.up_votes += 1
    
    # TODO: faster increment by counter type fields or raw sql
    def incr_clicks(self):
        """Increment 'clicks' by 1."""
        self.clicks += 1
    
    # TODO: faster increment by toogle type fields or raw sql
    def set_relevant(self, is_relevant=True):
        """Set 'is_relevant' value to True(deafult) or False."""
        self.is_relevant = is_relevant
    
    # TODO: tests
    # TODO: implement 
    def validate_url(self):
        """Check if the url is still valid."""
        raise NotImplementedError
    
    # TODO: tests
    def delete(self, *args, **kwargs):
        """Log the link data before deleting it."""
        logger.info('{%s} %s' % (__name__, self.__dict__))
        super(Link, self).delete(*args, **kwargs)