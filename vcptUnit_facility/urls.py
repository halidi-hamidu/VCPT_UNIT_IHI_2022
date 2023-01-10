from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_facility'

urlpatterns = [
   path('', views.facilityPage, name='facilityPage')
]
