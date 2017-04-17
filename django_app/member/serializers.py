from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from rest_framework import serializers

from content_api.serializers.bookmark import BookmarkedContentSerializer


class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):

    # user가 북마크한 content에 대한 상세한 정보를 가져오기 위해 추가적으로 설정 - 최영민
    bookmarks = BookmarkedContentSerializer(many=True, read_only=True)

    paginator = Paginator(bookmarks, 2)
    bookmarkss = paginator.page(1).object_list

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'bookmarks')
