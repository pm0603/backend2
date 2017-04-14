from rest_framework import serializers

from content_api.models import Content
from content_api.models.content import PostComment

__all__ = (
    'ContentDetailSerializer',
    'ContentSimpleSerializer',
)


class ContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'content', 'ticket_url', 'phone', 'thumbnail',
                  'place_url', 'place_addr', 'gps_x', 'gps_y')


class ContentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'thumbnail',)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'