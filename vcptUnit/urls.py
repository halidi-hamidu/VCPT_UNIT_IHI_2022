"""vcptUnit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vcptUnit_home.urls', namespace='vcptUnit_home')),
    path('vcptu-contact', include('vcptUnit_contact.urls', namespace='vcptUnit_contact')),
    path('about-vcptu', include('vcptUnit_aboutUs.urls', namespace='vcptUnit_aboutus')),
    path('vcptu-services', include('vcptUnit_service.urls', namespace='vcptUnit_service')),
    path('vcptu-facility', include('vcptUnit_facility.urls', namespace='vcptUnit_facility')),
    # path('vcptu-news', include('vcptUnit_news.urls', namespace='vcptUnit_news')),
    # path('vcptu-publication', include('vcptUnit_publication.urls', namespace='vcptUnit_publication')),
    # path('vcptu-reports', include('vcptUnit_reports.urls', namespace='vcptUnit_reports')),
    path('vcptu-team', include('vcptUnit_team.urls', namespace='vcptUnit_team')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
