from django.shortcuts import render, redirect, get_object_or_404
from vcptUnit_publication.models import VcptuPublications
# Create your views here.

def publicationPage(request):
    get_all_publication
    template_name = 'vcptUnit_publication/publicationPage.html'
    context = {

    }

    return  render(request, template_name, context)