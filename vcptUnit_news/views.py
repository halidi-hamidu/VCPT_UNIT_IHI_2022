from django.shortcuts import render

# Create your views here.
def newsPage(request):
    template_name = 'vcptUnit_news/newsPage.html'
    context = {
    }
    return render(request, template_name, context)

def detailaViewPage(request):
    template_name = 'vcptUnit_news/detailaViewPage.html'
    context = {
    }
    return render(request, template_name, context)

def headOfVectorControlDetailaViewPage(request):
    template_name = 'vcptUnit_news/headOfVectorControlDetailaViewPage.html'
    context = {
    }
    return render(request, template_name, context)