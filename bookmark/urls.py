from django.conf.urls import url

from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
  # Class-based views
  # bookmark list
  url(r'^$', BookmarkLV.as_view(), name='index'),
  # bookmark detail
  url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]