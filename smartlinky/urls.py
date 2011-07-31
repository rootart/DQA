from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('apps.api.urls')),
    url(r'^', include('apps.site.urls')),
    
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

