from django.contrib import admin

from blog.models import Post

# Register your models here.

# Post 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지 정의
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'create_date','modify_date') # Admin 리스트에서 보여줄 컬럼
  list_filter = ('modify_date',) # modify_date 컬럼을 사용하는 필터 사이드바를 보여주도록 지정
  search_fields = ('title', 'content') # 검색박스를 표시하고, 입력된 단어는 title과 content 컬럼에서 검색하도록 설정
  prepopulated_fields = {'slug':('title',)} # slug 필드를 title 필드를 사용해 미리 채워지도록 한다.

admin.site.register(Post, PostAdmin)