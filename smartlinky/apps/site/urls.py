from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('apps.site.views', 
    url(r'^about$', 'about', name='site_about'),
    url(r'^search$', 'search', name='site_search'),
    url(r'^$', 'index', name='site_index'),
    # TODO: create an example site with docs and Smartlinky functionality embedded
    url(r'^$', 'index', name='site_example'),
)



    
