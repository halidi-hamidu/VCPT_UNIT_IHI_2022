from django.shortcuts import render
from django import template
from django.conf import settings
from vcptUnit_news.models import VcptuNews
from vcptUnit_publication.models import VcptuPublications
# Create your views here.


def homePage(request):
    get_latest_publication = VcptuPublications.objects.all().order_by('updated_at')[:2]
    get_latest_news_or_latest_events = VcptuNews.objects.all().order_by('updated_at')[:3]
    template_name = 'vcptUnit_home/homePage.html'
    context = {
        'CURRENT_YEAR': settings.CURRENT_YEAR,
        'get_latest_news_or_latest_events':get_latest_news_or_latest_events,
        'get_latest_publication':get_latest_publication
    }
    return render(request, template_name, context)
