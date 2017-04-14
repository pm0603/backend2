from rest_framework import serializers

from content_api.models import Bookmark

__all__ = (
    'BookmarkSerializer',
)


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('user', 'content', 'description')