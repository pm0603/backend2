from django.contrib.auth import get_user_model
from django.db import models

from content_api.models import Content

__all__ = (
    'Bookmark',
)

User = get_user_model()


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    content = models.ForeignKey(Content)
    