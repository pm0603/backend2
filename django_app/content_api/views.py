from rest_framework import filters, permissions
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings

from content_api.models.content import ContentComment
from content_api.serializers.content import CommentSerializer
from content_api.utils import DefaultResultsSetPagination
from .models import Content
from .serializers import ContentDetailSerializer, ContentSimpleSerializer


# Pagination 개별 설정을 위한 클래스
class DefaultResultsSetPagination(PageNumberPagination):
    page_size = 6


class CommentPagination(PageNumberPagination):
    page_size = 10


# class CustomFilter(SearchFilter):
#     parameter_name = 'q'

# Content DB 정보 API
class ContentViewSet(viewsets.ReadOnlyModelViewSet, SearchFilter):
    queryset = Content.objects.all()

    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_param = api_settings.SEARCH_PARAM

    # 필터링 조건 (카테고리)
    filter_fields = ('seq', 'area', 'realm_name')

    # search 대상(통합검색)
    search_fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                     'area', 'price', 'content',)

    # 최신순 정렬
    ordering = ('-start_date', '-seq')

    # 한페이지당 6개의 아이템
    pagination_class = DefaultResultsSetPagination

    # 요청 조건에 따라 serializer 선택
    def get_serializer_class(self):
        if self.request.query_params.get('seq'):
            return ContentDetailSerializer
        else:
            return ContentSimpleSerializer

# 커맨트 뷰

class CommentViweSet(viewsets.ModelViewSet):
    queryset = ContentComment.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('content', 'id',)
    ordering = ('created_date',)
    serializer_class = CommentSerializer
    pagination_class = CommentPagination
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
