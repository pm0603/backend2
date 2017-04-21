from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Bookmark 관련 APIView로 list, create, delete 기능으로 구분 - 최영민
from rest_framework.response import Response
from rest_framework.views import APIView

from content_api.models import Bookmark
from content_api.models import Content
from content_api.serializers.bookmark import BookmarkSerializer
from content_api.utils import DefaultResultsSetPagination



# 한페이지당 6개의 아이템 표시 - 최영민
# 해당 user Bookmark만 보여주며 최신순으로 정렬 - 최영민
class BookmarkListView(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    pagination_class = DefaultResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        return user.bookmark_set.all().order_by('-created_date')


class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated, )

    # user정보를 따로 받을 필요 없이 user가 로그인 되면 로그인된 user정보를 활용 - 최영민
    def perform_create(self, serializer):
        content = Content.objects.get(id=self.request.data['content'])
        if Bookmark.objects.filter(user=self.request.user, content=content):
            raise ValueError
        else:
            serializer.save(
                user=self.request.user,
                content=content,
            )


class BookmarkDeleteView(APIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, format=None):
        content = Content.objects.get(id=self.request.data['content'])
        instance = Bookmark.objects.filter(user=self.request.user, content=content)
        instance.delete()
        return Response('deleted {}\'s bookmark {}'.format(self.request.user, instance))