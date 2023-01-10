from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_service'

urlpatterns = [
    path('', views.servicesPage, name='servicesPage')
]
