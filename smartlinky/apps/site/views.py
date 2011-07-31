from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.cache import never_cache, cache_page

from apps.core.models import Link


# TODO: tests
# TODO: docstrings
@never_cache
def index(request):
    """Main view of the site that also performs link feed."""
    
    ctx = {} 
    recent_links = Link.objects.all().order_by('created_at')[:4]
    ctx['feeds'] = recent_links
    
    return render_to_response('site/index.html', ctx, context_instance=RequestContext(request))

# TODO: tests
# TODO: docstrings
# TODO: caching
#@cache_page(60*60)
@never_cache
def about(request):
    """
    """
    return render_to_response('site/about.html', {}, context_instance=RequestContext(request))

@never_cache
def search(request):
    query = request.GET.get('q')
    ctx = {
        'search_results_pag': [],
        'feeds': [],
        'query': query
    }
    
    if query:
        # TODO: create a proper search query
        search_results = Link.objects.all()
        
        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1
    
        search_results_pag = Paginator(search_results, 3)
        try:
            search_results_pag = search_results_pag.page(page)
        except (EmptyPage, InvalidPage):
            search_results_pag = search_results_pag.page(search_results_pag.num_pages)

        ctx['search_results_pag'] = search_results_pag
    return render_to_response('site/search.html', ctx, context_instance=RequestContext(request))
