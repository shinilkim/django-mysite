from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.

# [A-01] ListView
class PostLV(ListView):
  model = Post
  template_name = 'blog/post_all.html' # 지정하지 않으면 디폴트로 post_list.html
  context_object_name = 'posts' # 템플릿에 넘겨주는 객체명 지정(디폴트 컨텍스트명 object_list 역시 사용 가능)
  paginate_by = 2 # 한 페이지에 보여줄 게시물 수(장고가 기본적으로 제공함)

# [A-02] DetailView
class PostDV(DetailView):
  model = Post

# [A-03-01] ArchiveIndexView
class PostAV(ArchiveIndexView):
  model = Post
  date_field = 'modify_date'

# [A-03-02] YearArchiveView
class PostYAV(YearArchiveView):
  model = Post
  date_field = 'modify_date'
  make_object_list = True

# [A-03-03] MonthArchiveView
class PostMAV(MonthArchiveView):
  model = Post
  date_field = 'modify_date'

# [A-03-04] DayArchiveView
class PostDAV(DayArchiveView):
  model = Post
  date_field = 'modify_date'

# [A-03-05] TodayArchiveView
class PostTAV(TodayArchiveView):
  model = Post
  date_field = "modify_date" # 변경 날짜가 오늘인 포스트 검색