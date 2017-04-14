from django.db import models

from config import settings

# 컨텐트 모델
from member.models import MyUser


class Content(models.Model):
    seq = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    place = models.TextField(null=True)
    realm_name = models.TextField(null=True)
    area = models.TextField(null=True)
    price = models.TextField(null=True)
    content = models.TextField(null=True)
    ticket_url = models.TextField(null=True)
    phone = models.TextField(null=True)
    thumbnail = models.TextField(null=True)
    gps_x = models.TextField(null=True)
    gps_y = models.TextField(null=True)
    place_url = models.TextField(null=True)
    place_addr = models.TextField(null=True)
    place_seq = models.TextField(null=True)
    # Comment는 추후에 구현 (최영민)
    comment = models.ManyToManyField(
        MyUser,
        through='PostComment',
        through_fields=('post', 'author'),
    )

# 리뷰 모델

class PostComment(models.Model):
    post = models.ForeignKey(Content)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()
    score = models.CharField(max_length=1, null=True)
    created_date = models.DateTimeField(auto_now_add=True)