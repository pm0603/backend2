from rest_framework import serializers

from content_api.models import Content
from content_api.models.content import PostComment

__all__ = (
    'ContentDetailSerializer',
    'ContentSimpleSerializer',
)


class ContentDetailSerializer(serializers.ModelSerializer):
    comment = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='username',
     )
    class Meta:
        model = Content
        fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'content', 'ticket_url', 'phone', 'thumbnail',
                  'place_url', 'place_addr', 'gps_x', 'gps_y', 'comment')


class ContentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'thumbnail',)



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'