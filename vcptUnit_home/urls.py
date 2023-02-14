from django.urls import path
from vcptUnit_home import views

# urlsPatterns

app_name = 'vcptUnit_home'

urlpatterns = [
    path('', views.homePage, name='homePage')
]
