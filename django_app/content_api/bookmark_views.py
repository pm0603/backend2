from rest_framework import generics


# Bookmark관련 ViewSet으로 list기능과 create, delete기능으로 구분 - 최영민
from content_api.models import Bookmark


class BookmarkViewSet(generics.ListAPIView):
    queryset = Bookmark.objects.all()

    # 최신순 정렬
    ordering = ('-start_date', '-seq')


class BookmarkUpdateViewSet(generics.C)