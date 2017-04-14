from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Bookmark관련 ViewSet으로 list기능과 create, delete기능으로 구분 - 최영민

from content_api.models import Bookmark
from content_api.serializers.bookmark import BookmarkSerializer


class BookmarkListView(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    # permission_classes = (IsAuthenticated, )

    # 최신순 정렬
    ordering = ('-start_date', '-seq')


class BookmarkCreateView(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    # permission_classes = (IsAuthenticated, )
