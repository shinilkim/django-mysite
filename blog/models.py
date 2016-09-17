# Python 2와 버전 3간에 문자열 처리하는 방식이 다르므로 호화성 확보
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

#from django.utils.text import slugify
from django.core.urlresolvers import reverse # URL 패턴을 만들어주는 장고 내장 함수
#from django.contrib.auth.models import User
from django.db import models

#from taggit.managers import TaggableManager

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
  title = models.CharField('TITLE', max_length=100)
  slug = models.SlugField('SLUG', max_length=100, unique=True, allow_unicode=True, help_text='one word for title alias.') # auto index create
  description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
  content = models.TextField('CONTENT')
  create_date = models.DateTimeField('Create Date', auto_now_add=True)
  modify_date = models.DateTimeField('Modify Date', auto_now=True)

  class Meta:
    verbose_name = 'post' # 테이블 별칭
    verbose_name_plural = 'posts' # 테이블의 복수 별칭
    db_table = 'blog_post' # 데이터베이스에 저장되는 테이블의 이름 지정
    ordering = ('-modify_date',) # 모델 개체의 리스트 출력 시 modify_date 컬럼을 기준으로 내림차순으로 정렬

  # 객체의 문자열 표현을 지정
  def __str__(self):
    return self.title
  # URL 반환
  def get_absolute_url(self):
    return reverse('blog:post_detail', args=(self.slug,))
  # modify_date 컬럼을 기준으로 이전 포스트를 반환(장고 내장함수)
  def get_previous_post(self):
    return self.get_previous_by_modify_date()
  # modify_date 컬럼을 기준으로 다음 포스트를 반환(장고 내장함수)
  def get_next_post(self):
    return self.get_next_by_modify_date()
