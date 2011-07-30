from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.api.views', 
    url(r'^init$', 'init', name='api_init'),
    url(r'^user_links$', 'user_links', name='api_user_links'),
    url(r'^qa_links$', 'qa_links', name='api_qa_init'),

    # TODO: remove when proper api views are working
    url(r'^demo_init$', 'demo_init', name='api_demo_init'),
    url(r'^demo_user_links$', 'demo_user_links', name='api_demo_user_links'),
    url(r'^demo_qa_links$', 'demo_qa_links', name='api_demo_qa_init'),
)

