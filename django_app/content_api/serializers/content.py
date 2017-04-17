from rest_framework import serializers

from content_api.models import Content
from content_api.models.content import ContentComment

__all__ = (
    'ContentDetailSerializer',
    'ContentSimpleSerializer',
)


# 전체 콘텐츠 출력시 기본정보만 나오는 시리얼라이저
class ContentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('id', 'seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                  'area', 'price', 'thumbnail')


# 상세페이지에서 추가 정보 불러오기 위한 필드(작업중)
class CommentListField(serializers.RelatedField):
    def to_representation(self, value):
        print(value)
        return 'review %s' % (value.username,)


# 상세 페이지 출력시 상세정보까지 나오는 시리얼라이저
class ContentDetailSerializer(serializers.ModelSerializer):
    comment_user = CommentListField(many=True, read_only=True)

    class Meta:
        model = Content
        fields = '__all__'

# 코멘트 시리얼라이저
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentComment
        fields = '__all__'