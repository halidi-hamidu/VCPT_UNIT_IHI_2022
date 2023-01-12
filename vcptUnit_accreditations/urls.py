from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_accreditations'

urlpatterns = [
    path('', views.accreditationPage, name='accreditationPage')
]
