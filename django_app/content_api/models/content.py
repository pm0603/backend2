from django.db import models

__all__ = (
    'Content',
)


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

    # DRF에서 구체적인 공연명을 알기 위한 설정 - 최영민
    def __str__(self):
        return self.title


        # Comment는 추후에 구현 (최영민)
        # comment = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

# class PostComment(models.Model):
#     post = models.ForeignKey(Content)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#     content = models.TextField()
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '{} comment (author:{}) \n {}'.format(
#             self.post_id,
#             self.author_id,
#             self.content
#         )
