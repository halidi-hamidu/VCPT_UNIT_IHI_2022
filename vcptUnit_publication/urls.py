from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_publication'

urlpatterns = [
    path('', views.publicationPage, name='publicationPage'),
    path('publicationPageDetail/<str:pub_year>/', views.publicationPageDetail, name='publicationPageDetail')
]
