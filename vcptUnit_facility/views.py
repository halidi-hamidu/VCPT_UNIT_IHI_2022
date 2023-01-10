from django.shortcuts import render

# Create your views here.
def facilityPage(request):
    template_name = 'vcptUnit_facility/facilityPage.html'
    context = {

    }
    return render(request, template_name, context)