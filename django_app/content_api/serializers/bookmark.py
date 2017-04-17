from rest_framework import serializers

from content_api.models import Bookmark
from content_api.models import Content

__all__ = (
    'BookmarkSerializer',
)


class BookmarkSerializer(serializers.ModelSerializer):
    # username = serializers.ModelField(model_field='user.username')
    # content_title = serializers.Field(source='content.title')

    content = serializers.CharField()

    class Meta:
        model = Bookmark
        fields = ('content', 'description')


# user가 북마크한 content에 대한 상세한 정보를 가져오기 위해 추가적으로 설정 - 최영민
class BookmarkedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'start_date', 'price')