from django.shortcuts import render

# Create your views here.

def galleryPage(request):
    template_name = 'vcptUnit_gallery/galleryPage.html'
    context = {
		
	}
    return render(request, template_name, context)