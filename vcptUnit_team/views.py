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


def SaraahMooredetailView(request):
    template_name = 'vcptUnit_team/SaraahMooredetailView.html'
    context = {

    }
    return render(request, template_name, context)

def JasonMooredetailView(request):
    template_name = 'vcptUnit_team/JasonMooredetailView.html'
    context = {

    }
    return render(request, template_name, context)

def swaiDetailView(request):
    template_name = 'vcptUnit_team/swaiDetailView.html'
    context = {

    }
    return render(request, template_name, context)