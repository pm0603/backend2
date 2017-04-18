from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from content_api.models import Content

__all__ = (
    'Bookmark',
)

User = settings.AUTH_USER_MODEL


# description은 추후 프론트팀이 가능하면 작업할 내용 - 최영민

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    description = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = (('user', 'content'),)
        ordering = ['-created_date']

    # UserDetail에서 북마크 정보 확인 시 최신 순으로 보기 위해 설정 - 최영민
        ordering = ['-created_date']

    def __str__(self):
        return '{} bookmarked by user {}'.format(self.content, self.user)