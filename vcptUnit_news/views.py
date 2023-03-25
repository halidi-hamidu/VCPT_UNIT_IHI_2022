from django.shortcuts import render

# Create your views here.
def newsPage(request):
    template_name = 'vcptUnit_news/newsPage.html'
    context = {
    }
    return render(request, template_name, context)

def engagementdetailaViewPage(request):
    template_name = 'vcptUnit_news/engagementdetailaViewPage.html'
    context = {
    }
    return render(request, template_name, context)

def detailaViewPage(request):
    template_name = 'vcptUnit_news/detailaViewPage.html'
    context = {
    }
    return render(request, template_name, context)

def headOfVectorControl(request):
    template_name = 'vcptUnit_news/headOfVectorControl.html'
    context = {
    }
    return render(request, template_name, context)
        
def engagementNewsDetailView(request):
    template_name = 'vcptUnit_news/engagementNewsDetailView.html'
    context = {
    }
    return render(request, template_name, context)

def headOfVectorControlFullDetailViewPage(request):
    template_name = 'vcptUnit_news/headOfVectorControlFullDetailViewPage.html'
    context = {
    }
    return render(request, template_name, context)