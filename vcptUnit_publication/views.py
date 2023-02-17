from django.shortcuts import render, redirect, get_object_or_404
from vcptUnit_publication.models import VcptuPublications
# Create your views here.

def publicationPage(request):
    get_all_publication = VcptuPublications.objects.all()
    my_empty_list = []
    distinct_year_in_list = []
    for publication_year in get_all_publication:
        my_empty_list.append(publication_year.publication_year)
        if not publication_year.publication_year in distinct_year_in_list:
            distinct_year_in_list.append(publication_year.publication_year)
    print("yers", distinct_year_in_list)        
    template_name = 'vcptUnit_publication/publicationPage.html'
    context = {
        'get_all_publication':get_all_publication,
        'distinct_year_in_list':distinct_year_in_list
    }

    return  render(request, template_name, context)

def publicationPageDetail(request, pub_year ):
    
    get_publication_from_specific_year = VcptuPublications.objects.filter(publication_year = pub_year)
    get_all_publication = VcptuPublications.objects.all()
    my_empty_list = []
    distinct_year_in_list = []
    for publication_year in get_all_publication:
        my_empty_list.append(publication_year.publication_year)
        if not publication_year.publication_year in distinct_year_in_list:
            distinct_year_in_list.append(publication_year.publication_year)
    
    template_name = 'vcptUnit_publication/publicationPage.html'
    context = {
    'get_publication_from_specific_year':get_publication_from_specific_year,
    'distinct_year_in_list':distinct_year_in_list,
    'pub_year':pub_year,
    }

    return  render(request, template_name, context)