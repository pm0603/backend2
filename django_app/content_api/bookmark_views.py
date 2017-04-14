from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Bookmark 관련 APIView로 list, create, delete 기능으로 구분 - 최영민

from content_api.models import Bookmark
from content_api.serializers.bookmark import BookmarkSerializer
from content_api.utils import DefaultResultsSetPagination


class BookmarkListView(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    # 한페이지당 6개의 아이템 표시 - 최영민
    pagination_class = DefaultResultsSetPagination

    # 해당 user Bookmark만 보여주며 최신순으로 정렬 - 최영민
    def get_queryset(self):
        user = self.request.user
        return user.bookmark_set.all().order_by('-created_date')


class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated, )


class BookmarkDeleteView(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated, )