from django.contrib.auth import get_user_model
from django.db import models

from config import settings

__all__ = (
    'Content',
)

# User모델 가져오기 - 최영민
User = get_user_model()


class Content(models.Model):
    seq = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    place = models.TextField(blank=True)
    realm_name = models.CharField(max_length=5,null=True)
    area = models.CharField(max_length=5, null=True)
    price = models.CharField(max_length=30, null=True)
    content = models.TextField(blank=True)
    ticket_url = models.TextField(blank=True)
    phone = models.CharField(max_length=50, null=True)
    thumbnail = models.TextField(blank=True)
    place_url = models.TextField(blank=True)
    place_addr = models.CharField(max_length=6, null=True)
    place_seq = models.TextField(blank=True)

    # 중간자 모델인 Bookmark를 이용해 User와 연결 - 최영민
    bookmarks = models.ManyToManyField(User, through='Bookmark')

    # DRF에서 구체적인 공연명을 알기 위한 설정 - 최영민
    def __str__(self):
        return self.title

    # # Comment는 추후에 구현 (최영민)
    # comment_user = models.ManyToManyField(
    #     User,
    #     through='ContentComment',
    #     related_name='comment_relate',
    # )


# 리뷰 모델
class ContentComment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
