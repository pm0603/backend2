from rest_framework import serializers

from content_api.models import Bookmark
from content_api.models import Content

__all__ = (
    'BookmarkSerializer',
    'BookmarkedContentSerializer',
)


# user가 북마크한 content에 대한 상세한 정보를 가져오기 위해 추가적으로 설정 - 최영민
class BookmarkedContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ('title', 'start_date', 'price')


class BookmarkSerializer(serializers.ModelSerializer):

    content = serializers.IntegerField(source='content.id')
    seq = serializers.CharField(source='content.seq', required=False)
    title = serializers.CharField(source='content.title', required=False)
    price = serializers.CharField(source='content.price', required=False)
    start_date = serializers.DateField(source='content.start_date', required=False)
    end_date = serializers.DateField(source='content.end_date', required=False)
    area = serializers.CharField(source='content.area', required=False)
    place = serializers.CharField(source='content.place', required=False)

    class Meta:
        model = Bookmark
        fields = ('content', 'title', 'price', 'area', 'place', 'start_date', 'end_date', 'seq')
