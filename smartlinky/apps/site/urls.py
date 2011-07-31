from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('apps.site.views', 
    url(r'^about$', direct_to_template, {'template': 'site/about.html'}, name='site_about'),
    url(r'^$', direct_to_template, {'template': 'site/index.html'}, name='site_index'),
)



    