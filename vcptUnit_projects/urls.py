from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_projects'

urlpatterns = [
    path('', views.projectPage, name='projectPage')
]
