from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_team'

urlpatterns = [
   path('', views.teamPage, name='teamPage'),
   path('staff-detail', views.detailView, name='detailView'),
]
