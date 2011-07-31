from django.conf import settings
from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
    url(r'^api/', include('apps.api.urls')),
    url(r'^', include('apps.site.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

