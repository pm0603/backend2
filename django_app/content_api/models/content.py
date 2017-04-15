from django.contrib.auth import get_user_model
from django.db import models

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

    # 중간자 모델인 Bookmark를 이용해 User와 연결 - 최영민
    bookmarks = models.ManyToManyField(User, through='Bookmark')

    # DRF에서 구체적인 공연명을 알기 위한 설정 - 최영민
    def __str__(self):
        return self.title

    # Comment는 추후에 구현 (최영민)
    comment = models.ManyToManyField(
        User,
        through='PostComment',
        related_name='comment_relate',
    )


# 리뷰 모델
class PostComment(models.Model):
    post = models.ForeignKey(Content, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    score = models.CharField(max_length=1, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s: %s \n 별점: %c, 작성일: %s' % (self.author_id, self.body, self.score, self.created_date)
