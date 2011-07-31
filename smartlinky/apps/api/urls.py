from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('apps.api.views', 
    url(r'^init$', 'init', name='api_init'),
    url(r'^users_links$', 'users_links', name='api_users_links'),
    url(r'^qa_links$', 'qa_links', name='api_qa_links'),
    url(r'^add_link$', 'add_link', name='api_add_link'),
    url(r'^vote_up$', 'vote_up', name='api_vote_up'),
    url(r'^set_relevant$', 'set_relevant', name='api_set_relevant'),
)

