from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.api.views', 
    url(r'^demo/init$', 'demo_init'),
    url(r'^demo/get_section$', 'demo_get_section'),
)

