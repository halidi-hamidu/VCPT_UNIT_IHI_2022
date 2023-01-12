from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_news'

urlpatterns = [
    path('', views.newsPage, name='newsPage')
]
