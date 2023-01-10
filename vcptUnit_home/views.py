from django.shortcuts import render
from django import template
from django.conf import settings
# Create your views here.


def homePage(request):
    template_name = 'vcptUnit_home/homePage.html'
    context = {
        'CURRENT_YEAR': settings.CURRENT_YEAR
    }
    return render(request, template_name, context)
