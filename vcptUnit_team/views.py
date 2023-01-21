from django.shortcuts import render

# Create your views here.
def teamPage(request):
    template_name = 'vcptUnit_team/teamPage.html'
    context = {

    }
    return render(request, template_name, context)


def detailView(request):
    template_name = 'vcptUnit_team/detailView.html'
    context = {

    }
    return render(request, template_name, context)
