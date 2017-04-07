from django.db import models


class Performance(models.Model):
    seq = models.CharField(max_length=20, unique=True)
    title = models.TextField()
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
# comment = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
#
#
# class Comment(models.Model):
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
