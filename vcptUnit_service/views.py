from django.shortcuts import render
from django import template
from django.conf import settings

# Create your views here.
def servicesPage(request):
    template_name = 'vcptUnit_service/servicesPage.html'
    context = {
        'CURRENT_YEAR': settings.CURRENT_YEAR
    }
    return render(request, template_name, context)
