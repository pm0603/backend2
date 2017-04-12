from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination

from .models import Content
from .serializers import ContentDetailSerializer, ContentSimpleSerializer

# Pagination 개별 설정을 위한 클래스
class DefaultResultsSetPagination(PageNumberPagination):
    page_size = 6


# Content DB 정보 API
class ContentViewSet(generics.ListAPIView):
    queryset = Content.objects.all()
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)

    # 필터링 조건 (카테고리)
    filter_fields = ('seq', 'area', 'realm_name')

    # 최신순 정렬
    ordering = ('-start_date', '-seq')

    # 한페이지당 6개의 아이템
    pagination_class = DefaultResultsSetPagination

    # 요청 조건에 따라 serializer 선택
    def get_serializer_class(self):
        if self.request.query_params.get('seq'):
            return ContentDetailSerializer
        elif self.request.query_params.get('realm_name'):
            return ContentSimpleSerializer
        elif self.request.query_params.get('area'):
            return ContentSimpleSerializer
