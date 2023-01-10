from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_aboutus'

urlpatterns = [
    path('', views.aboutPage, name='aboutPage')
]
