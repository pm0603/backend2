from django.conf import settings
from django.db import models

from config import settings


class Content(models.Model):
    seq = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.CharField(max_length=100, null=True)
    realm_name = models.CharField(max_length=50, null=True)
    area = models.CharField(max_length=10, null=True)
    price = models.models.TextField()
    content = models.TextField()
    ticket_url = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=50, null=True)
    thumbnail = models.CharField(max_length=200, null=True)
    gps_x = models.CharField(max_length=30, null=True)
    gps_y = models.CharField(max_length=30, null=True)
    place_url = models.CharField(max_length=200, null=True)
    place_addr = models.CharField(max_length=100, null=True)
    place_seq = models.CharField(max_length=10, null=True)
    comment = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)


class PostComment(models.Model):
    post = models.ForeignKey(Content)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} comment (author:{}) \n {}'.format(
            self.post_id,
            self.author_id,
            self.content
        )
