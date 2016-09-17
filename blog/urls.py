from django.conf.urls import url
from blog.views import *

urlpatterns = [
  # 블로그 목록(일반) [/blog/] => blog:index
  url(r'^$', PostLV.as_view(), name='index'),
  # 블로그 목록(일반) [/blog/post/] (same as /) => blog:post_list
  url(r'^post/$', PostLV.as_view(), name='post_list'),
  # 블로그 상세 [/blog/post/django-example/] => blog:post_detail
  url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
  # 블로그 목록(날짜별로 구분) [/blog/archive/] => blog:post_archive
  url(r'^archive/$', PostAV.as_view(), name='post_archive'),
  # [/blog/2016/] => blog:post_year_archive
  url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
  # [/blog/2016/nov/] => blog:post_month_archive
  url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
  # [/blog/2016/nov/10] => post_day_archive
  url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
  # [/blog/today/] => blog:post_today_archive
  url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
]