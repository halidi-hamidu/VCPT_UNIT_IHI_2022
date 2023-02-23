from django.urls import path
from . import views

# urlsPatterns

app_name = 'vcptUnit_team'

urlpatterns = [
   path('', views.teamPage, name='teamPage'),
   path('staff-detail', views.detailView, name='detailView'),
   path('staff-detail-dr-saraah-Moore', views.SaraahMooredetailView, name='SaraahMooredetailView'),
   path('staff-detail-jason-Moore', views.JasonMooredetailView, name='JasonMooredetailView'),
   path('staff-detail-kyeba-swai', views.swaiDetailView, name='swaiDetailView'),
   
]
