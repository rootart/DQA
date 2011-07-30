from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^api/', include('apps.api.urls')),
    url(r'^$', direct_to_template, {'template': 'index.html'}, name='index'),
    url(r'^about$', direct_to_template, {'template': 'about.html'}, name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

