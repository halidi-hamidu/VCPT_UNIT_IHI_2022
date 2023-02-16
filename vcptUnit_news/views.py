from django.shortcuts import render, redirect, get_object_or_404
from vcptUnit_news.models import VcptuNews
# Create your views here.
def newsPage(request):
    get_latest_news_or_latest_events = VcptuNews.objects.all().order_by('updated_at')
    get_one_latest_news_or_one_latest_events = VcptuNews.objects.all().order_by('updated_at').first
    template_name = 'vcptUnit_news/newsPage.html'
    context = {
    'get_latest_news_or_latest_events':get_latest_news_or_latest_events,
    'get_one_latest_news_or_one_latest_events':get_one_latest_news_or_one_latest_events
    }
    
    return render(request, template_name, context)

def detailaViewPage(request, id):
    
    get_news_or_event_detail= get_object_or_404(VcptuNews, id=id)
    template_name = 'vcptUnit_news/detailaViewPage.html'
    context = {
        'get_news_or_event_detail':get_news_or_event_detail
    }
    return render(request, template_name, context)