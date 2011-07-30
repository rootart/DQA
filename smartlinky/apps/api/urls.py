from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.api.views', 
    url(r'^init$', 'init', name='api_init'),
    url(r'^user_links$', 'user_links', name='api_user_links'),
    url(r'^qa_links$', 'qa_links', name='qa_links'),
    url(r'^add_link$', 'add_link', name='api_add_link'),
)

