from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_news'

urlpatterns = [
    path('', views.newsPage, name='newsPage'),
    path('detail-view/<str:id>/', views.detailaViewPage, name='detailaViewPage'),
]
