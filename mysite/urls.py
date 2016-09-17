"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import ListView, DetailView

from bookmark.models import Bookmark


urlpatterns = [
    # url(regex, view, kwargs=None, name=None, prefix='')
    url(r'^admin/', include(admin.site.urls)),

    # Class-based views for Bookmark app
    url(r'^bookmark/$', ListView.as_view(model=Bookmark), name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
