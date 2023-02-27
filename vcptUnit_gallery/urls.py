from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_gallery'

urlpatterns = [
    path('', views.galleryPage, name='galleryPage'),
   
]
