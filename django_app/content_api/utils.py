from rest_framework.pagination import PageNumberPagination

# Bookmark에서도 활용하기 위해 위치 변경 - 최영민
# Pagination 개별 설정을 위한 클래스 - 김도경

class DefaultResultsSetPagination(PageNumberPagination):
    page_size = 6