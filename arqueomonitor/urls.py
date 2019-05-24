"""arqueomonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from arqueomonitor.apps.campaign import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.start, name='home'),
    url(r'^byThePlots/$', views.byThePlots, name='byThePlots'),
    url(r'^addCruise/$', views.addCruise, name='addCruise'),
    url(r'^addStation/$', views.addStation, name='addStation'),
    url(r'^getCruises/$', views.getCruises, name='getCruises'),
    url(r'^getDeployments/$', views.getDeployments, name='getDeployments'),
    url(r'^getSations/$', views.getStations, name='getStations'),
    url(r'^getInstruments/$', views.getInstruments, name='getInstruments'),
    url(r'^getSamples/$', views.getSamples, name='getSamples'),
    url(r'^getTankTrials/$', views.getTankTrials, name='getTankTrials'),
    url(r'^tablesDynamic/$', views.tablesDynamic, name='tablesDynamic'),
    url(r'^logIn/$', views.logIn, name='logIn'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
