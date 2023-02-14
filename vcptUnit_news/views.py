from django.shortcuts import render, redirect, get_object_or_404
from vcptUnit_news.models import VcptuNews
# Create your views here.
def newsPage(request):
    template_name = 'vcptUnit_news/newsPage.html'
    context = {
    }
    return render(request, template_name, context)

def detailaViewPage(request, id):
    get_news_or_event_detail= get_object_or_404(VcptuNews, id=id)
    template_name = 'vcptUnit_news/detailaViewPage.html'
    context = {
        'get_news_or_event_detail':get_news_or_event_detail
    }
    return render(request, template_name, context)