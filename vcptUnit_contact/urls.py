from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_contact'

urlpatterns = [
    path('', views.contactPage, name='contactPage')
]
