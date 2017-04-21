from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from content_api import views
from content_api.bookmark_views import BookmarkListView, BookmarkCreateView, BookmarkDeleteView
from . import open_api

# 뷰셋 라우터 설정 - 김도경
router = DefaultRouter()
router.register(r'_content', views.ContentViewSet)
router.register(r'_comment', views.CommentViweSet)

urlpatterns = [
    # 지역별 검색 DB 추가 - 김도경
    url(r'db_save_area/', open_api.Area.as_view()),
    # 분야별 검색 DB 추가 - 김도경
    url(r'db_save_genre/', open_api.Genre.as_view()),
    # 라우터 루트 - 김도경
    url(r'^', include(router.urls)),

    # Bookmark 관련 url 설정 - 최영민
    url(r'bookmark/list', BookmarkListView.as_view()),
    url(r'bookmark/create', BookmarkCreateView.as_view()),
    url(r'bookmark/delete', BookmarkDeleteView.as_view()),
]