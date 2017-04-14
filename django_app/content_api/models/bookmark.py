from django.contrib.auth import get_user_model
from django.db import models

from content_api.models import Content

__all__ = (
    'Bookmark',
)

User = get_user_model()


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return '{} bookmarked by user {}'.format(self.content, self.user)