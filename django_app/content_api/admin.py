from django.contrib import admin

# Register your models here.
from content_api.models import Content

# Content 내용을 admin에서 확인하기 위해 설정 (최영민)
admin.site.register(Content)