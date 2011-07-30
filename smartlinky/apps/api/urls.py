from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.api.views', 
    url(r'^demo/init$', 'demo_init'),
    url(r'^demo/user_links$', 'demo_user_links'),
    url(r'^demo/qa_links$', 'demo_qa_links'),
)

