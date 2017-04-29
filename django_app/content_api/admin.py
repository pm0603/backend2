from django.contrib import admin

from content_api.models import Content, Bookmark
from content_api.models.content import ContentComment

# Content와 Bookmark내용을 admin에서 확인하기 위해 설정 - 최영민
admin.site.register(Content)
admin.site.register(ContentComment)
admin.site.register(Bookmark)
