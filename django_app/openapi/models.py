from django.db import models


class Content(models.Model):
    seq = models.CharField(max_length=20, unique=True)
    title = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    place = models.TextField()
    realm_name = models.TextField()
    area = models.TextField()
    price = models.TextField()
    content = models.TextField()
    ticket_url = models.TextField()
    phone = models.TextField()
    thumbnail = models.TextField()
    gps_x = models.TextField()
    gps_y = models.TextField()
    place_url = models.TextField()
    place_addr = models.TextField()
    place_seq = models.TextField()
# comment = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
#
#
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
