from django.conf.urls import url

from content_api.bookmark_views import BookmarkListView, BookmarkCreateView
from . import open_api
from .views import ContentViewSet

urlpatterns = [
    # Content DB API
    url(r'api/', ContentViewSet.as_view()),
    # 지역별 검색 DB 추가
    url(r'db_save_area/', open_api.Area.as_view()),
    # 분야별 검색 DB 추가
    url(r'db_save_genre/', open_api.Genre.as_view()),

    # Bookmark관련 url 설정 - 최영민
    url(r'^bookmark/', BookmarkListView.as_view()),
    url(r'^bookmark/', BookmarkCreateView()),
]
