from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_news'

urlpatterns = [
    path('', views.newsPage, name='newsPage'),
    path('-corporate-social-responsibility', views.detailaViewPage, name='detailaViewPage'),
    path('-head-of-vectors-from-nmcp-visited-vcptu', views.headOfVectorControl, name='headOfVectorControl'),
    path('-engagement-of-ifakara-show-case', views.engagementNewsDetailView, name='engagementNewsDetailView'),
    path('-engagement-of-ifakara', views.engagementdetailaViewPage, name='engagementdetailaViewPage'),
    path('-head-of-control', views.headOfVectorControlFullDetailViewPage , name='headOfVectorControlFullDetailViewPage'),
]
