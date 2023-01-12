from django.shortcuts import render

# Create your views here.

def accreditationPage(request):
    template_name = 'vcptUnit_accreditations/accreditationPage'
    context = {

    }
    return render(request, template_name, context)