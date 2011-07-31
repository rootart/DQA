from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('apps.site.views', 
    url(r'^about$', 'about', name='site_about'),
    url(r'^search$', 'search', name='site_search'),
    url(r'^example$', direct_to_template, {'template': 'site/example.html'}, name='site_example'),
    url(r'^$', 'index', name='site_index'),
)



    
