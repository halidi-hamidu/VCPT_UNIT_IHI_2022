from django.shortcuts import render

# Create your views here.

def publicationPage(request):
    template_name = 'vcptUnit_publication/publicationPage.html'
    context = {

    }

    return  render(request, template_name, context)